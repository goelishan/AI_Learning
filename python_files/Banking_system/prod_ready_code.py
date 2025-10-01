"""
Production-ready banking module (single-file).
Features:
 - Decimal-based money arithmetic
 - SQLite persistence for accounts and transactions
 - Atomic transfers with DB transactions and rollback
 - Per-account threading locks for concurrency safety
 - Savings and Current account types (inheritance)
 - Explicit exceptions and logging
"""

from __future__ import annotations
import sqlite3
from decimal import Decimal, getcontext, ROUND_HALF_UP
from threading import Lock, RLock
from typing import Dict, Optional, Tuple
from dataclasses import dataclass
import datetime
import logging
import uuid
import os

# ---------- Configuration ----------
getcontext().prec = 28  # Decimal precision
MONEY_QUANT = Decimal("0.01")

DB_PATH = "C:/Users/igoel/Desktop/AI_Learning/practise_code/python_files/Banking_system/bank.db"
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("banking")

# ---------- Exceptions ----------
class BankingError(Exception):
    pass

class InsufficientFundsError(BankingError):
    pass

class InvalidTransactionError(BankingError):
    pass

class AccountNotFoundError(BankingError):
    pass

class AccountAlreadyExistsError(BankingError):
    pass

# ---------- Helpers ----------
def to_decimal(value) -> Decimal:
    d = Decimal(str(value))
    return d.quantize(MONEY_QUANT, rounding=ROUND_HALF_UP)

def now_iso() -> str:
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

# ---------- Persistence / DB Layer ----------
class DB:
    def __init__(self, path: str = DB_PATH):
        exists = os.path.exists(path)
        self.conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None)  # autocommit off by manual BEGIN
        self.conn.execute("PRAGMA foreign_keys = ON;")
        if not exists:
            self._init_schema()

    def _init_schema(self):
        cur = self.conn.cursor()
        cur.executescript(
            """
            CREATE TABLE accounts (
                acc_number INTEGER PRIMARY KEY,
                acc_type TEXT NOT NULL,
                owner TEXT NOT NULL,
                balance TEXT NOT NULL, -- Decimal as string
                interest_rate TEXT,
                overdraft_limit TEXT
            );

            CREATE TABLE transactions (
                tx_id TEXT PRIMARY KEY,
                acc_number INTEGER NOT NULL,
                tx_type TEXT NOT NULL,
                amount TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                balance_after TEXT NOT NULL,
                meta TEXT,
                FOREIGN KEY(acc_number) REFERENCES accounts(acc_number)
            );
            """
        )
        self.conn.commit()
        logger.info("Database schema created")

    def execute(self, sql: str, params: Tuple = ()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur

    # transaction context manager
    def transaction(self):
        class _Tx:
            def __init__(self, conn):
                self.conn = conn
            def __enter__(self):
                self.conn.execute("BEGIN IMMEDIATE;")
                return self.conn
            def __exit__(self, exc_type, exc, tb):
                if exc_type is None:
                    self.conn.commit()
                else:
                    self.conn.rollback()
        return _Tx(self.conn)

# ---------- Account classes ----------
@dataclass
class AccountData:
    acc_number: int
    acc_type: str
    owner: str
    balance: Decimal
    interest_rate: Optional[Decimal] = None
    overdraft_limit: Optional[Decimal] = None

class BankAccount:
    def __init__(self, data: AccountData, bank: "Bank"):
        self._data = data
        # bank reference used for persistence & logging
        self._bank = bank

    @property
    def acc_number(self) -> int:
        return self._data.acc_number

    @property
    def owner(self) -> str:
        return self._data.owner

    @property
    def balance(self) -> Decimal:
        return self._data.balance

    def deposit(self, amount) -> Decimal:
        amt = to_decimal(amount)
        if amt <= 0:
            raise InvalidTransactionError("Deposit amount must be positive")
        # Use bank-level persistence to atomically write transaction
        new_balance = self._bank._apply_account_delta(self.acc_number, amt, "deposit")
        logger.info("Deposit: acc=%s amount=%s new_balance=%s", self.acc_number, amt, new_balance)
        return new_balance

    def withdraw(self, amount) -> Decimal:
        amt = to_decimal(amount)
        if amt <= 0:
            raise InvalidTransactionError("Withdrawal amount must be positive")
        # Business rule: base class disallows overdraft
        if amt > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        new_balance = self._bank._apply_account_delta(self.acc_number, -amt, "withdraw")
        logger.info("Withdraw: acc=%s amount=%s new_balance=%s", self.acc_number, amt, new_balance)
        return new_balance

    def transfer(self, target_acc_number: int, amount) -> None:
        if target_acc_number == self.acc_number:
            raise InvalidTransactionError("Cannot transfer to same account")
        self._bank.transfer(self.acc_number, target_acc_number, amount)

    def __str__(self):
        return f"{self.__class__.__name__}(Acc:{self.acc_number}, Owner:{self.owner}, Balance:{self.balance})"

class SavingsAccount(BankAccount):
    def add_interest(self) -> Decimal:
        if self._data.interest_rate is None:
            raise InvalidTransactionError("Interest rate not set for this account")
        interest = (self.balance * self._data.interest_rate).quantize(MONEY_QUANT, rounding=ROUND_HALF_UP)
        new_balance = self._bank._apply_account_delta(self.acc_number, interest, "interest")
        logger.info("Interest added: acc=%s interest=%s new_balance=%s", self.acc_number, interest, new_balance)
        return interest

class CurrentAccount(BankAccount):
    def withdraw(self, amount) -> Decimal:
        amt = to_decimal(amount)
        if amt <= 0:
            raise InvalidTransactionError("Withdrawal amount must be positive")
        overdraft = self._data.overdraft_limit or Decimal("0.00")
        if amt > (self.balance + overdraft):
            raise InsufficientFundsError("Exceeds overdraft limit")
        new_balance = self._bank._apply_account_delta(self.acc_number, -amt, "withdraw")
        logger.info("CurrentAccount withdraw: acc=%s amount=%s new_balance=%s", self.acc_number, amt, new_balance)
        return new_balance

# ---------- Bank (manager) ----------
class Bank:
    def __init__(self, name: str, db_path: str = DB_PATH):
        self.name = name
        self.db = DB(db_path)
        # locks for in-memory concurrency; RLock for nested operations
        self._locks: Dict[int, RLock] = {}
        # protect lock map
        self._locks_map_lock = Lock()

    # --------- Account factory & existence ----------
    def create_account(self, acc_number: int, owner: str, acc_type: str = "savings",
                       initial_deposit=0, interest_rate: Optional[float] = None,
                       overdraft_limit: Optional[float] = None) -> BankAccount:
        if self._account_exists(acc_number):
            raise AccountAlreadyExistsError("Account already exists")

        bal = to_decimal(initial_deposit)
        ir = to_decimal(interest_rate) if interest_rate is not None else None
        od = to_decimal(overdraft_limit) if overdraft_limit is not None else None

        with self.db.transaction():
            self.db.execute(
                "INSERT INTO accounts (acc_number, acc_type, owner, balance, interest_rate, overdraft_limit) VALUES (?, ?, ?, ?, ?, ?)",
                (acc_number, acc_type, owner, format(bal), format(ir) if ir is not None else None, format(od) if od is not None else None)
            )
            # initial ledger entry if deposit > 0
            if bal > 0:
                tx_id = str(uuid.uuid4())
                self.db.execute(
                    "INSERT INTO transactions (tx_id, acc_number, tx_type, amount, timestamp, balance_after, meta) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (tx_id, acc_number, "deposit", format(bal), now_iso(), format(bal), "initial_deposit")
                )

        account = self._load_account_object(acc_number)
        logger.info("Created account %s (%s) owner=%s", acc_number, acc_type, owner)
        return account

    def _account_exists(self, acc_number: int) -> bool:
        cur = self.db.execute("SELECT 1 FROM accounts WHERE acc_number = ? LIMIT 1", (acc_number,))
        return cur.fetchone() is not None

    def _load_account_object(self, acc_number: int) -> BankAccount:
        cur = self.db.execute("SELECT acc_number, acc_type, owner, balance, interest_rate, overdraft_limit FROM accounts WHERE acc_number = ?", (acc_number,))
        row = cur.fetchone()
        if not row:
            raise AccountNotFoundError("Account not found")
        acc_number, acc_type, owner, balance_s, ir_s, od_s = row
        data = AccountData(
            acc_number=int(acc_number),
            acc_type=acc_type,
            owner=owner,
            balance=to_decimal(balance_s),
            interest_rate=to_decimal(ir_s) if ir_s is not None else None,
            overdraft_limit=to_decimal(od_s) if od_s is not None else None
        )
        if acc_type == "savings":
            return SavingsAccount(data, self)
        elif acc_type == "current":
            return CurrentAccount(data, self)
        else:
            return BankAccount(data, self)

    def get_account(self, acc_number: int) -> BankAccount:
        return self._load_account_object(acc_number)

    # --------- Concurrency helpers ----------
    def _get_lock_for(self, acc_number: int) -> RLock:
        with self._locks_map_lock:
            if acc_number not in self._locks:
                self._locks[acc_number] = RLock()
            return self._locks[acc_number]

    # --------- Core persistence operation: apply delta (atomic per-account) ----------
    def _apply_account_delta(self, acc_number: int, delta: Decimal, tx_type: str, meta: Optional[str] = None) -> Decimal:
        """
        Safely apply a delta (positive for deposit/interest, negative for withdraw) to the account balance.
        This function:
         - obtains the account lock (to prevent concurrent in-memory races)
         - does a DB transaction to read, update balance and insert ledger row atomically.
        Returns new balance as Decimal.
        """
        lock = self._get_lock_for(acc_number)
        with lock:
            with self.db.transaction():
                cur = self.db.execute("SELECT balance FROM accounts WHERE acc_number = ? FOR UPDATE", (acc_number,))
                row = cur.fetchone()
                if not row:
                    raise AccountNotFoundError("Account not found")
                current_balance = to_decimal(row[0])
                new_balance = (current_balance + delta).quantize(MONEY_QUANT, rounding=ROUND_HALF_UP)
                # Business rule: do not allow negative balance unless account type permits overdraft.
                # For simplicity, check account type:
                acc_row = self.db.execute("SELECT acc_type, overdraft_limit FROM accounts WHERE acc_number = ?", (acc_number,)).fetchone()
                acc_type = acc_row[0]
                overdraft_limit = to_decimal(acc_row[1]) if acc_row[1] is not None else Decimal("0.00")
                if new_balance < Decimal("0.00") and acc_type != "current":
                    raise InsufficientFundsError("Insufficient funds (and no overdraft allowed)")
                if new_balance < -overdraft_limit:
                    raise InsufficientFundsError("Exceeds overdraft limit")
                # persist new balance
                self.db.execute("UPDATE accounts SET balance = ? WHERE acc_number = ?", (format(new_balance), acc_number))
                # ledger entry
                tx_id = str(uuid.uuid4())
                self.db.execute(
                    "INSERT INTO transactions (tx_id, acc_number, tx_type, amount, timestamp, balance_after, meta) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (tx_id, acc_number, tx_type, format(delta.copy_abs()), now_iso(), format(new_balance), meta)
                )
            # commit succeeded
            # Return re-loaded Decimal
            return new_balance

    # --------- Transfer (atomic across two accounts) ----------
    def transfer(self, from_acc: int, to_acc: int, amount) -> None:
        if from_acc == to_acc:
            raise InvalidTransactionError("Cannot transfer to same account")
        amt = to_decimal(amount)
        if amt <= 0:
            raise InvalidTransactionError("Transfer amount must be positive")

        # Acquire the two locks in a consistent order to avoid deadlocks (lower acc_number first)
        first, second = (from_acc, to_acc) if from_acc < to_acc else (to_acc, from_acc)
        lock1 = self._get_lock_for(first)
        lock2 = self._get_lock_for(second)

        with lock1:
            with lock2:
                # Use a DB transaction that updates both accounts atomically.
                with self.db.transaction():
                    # re-check existence & balances
                    cur = self.db.execute("SELECT balance, acc_type, overdraft_limit FROM accounts WHERE acc_number = ?", (from_acc,))
                    row = cur.fetchone()
                    if not row:
                        raise AccountNotFoundError("Source account not found")
                    from_balance = to_decimal(row[0])
                    from_type = row[1]
                    from_overdraft = to_decimal(row[2]) if row[2] is not None else Decimal("0.00")

                    cur2 = self.db.execute("SELECT balance, acc_type, overdraft_limit FROM accounts WHERE acc_number = ?", (to_acc,))
                    row2 = cur2.fetchone()
                    if not row2:
                        raise AccountNotFoundError("Target account not found")
                    to_balance = to_decimal(row2[0])

                    # check source allowed to send amt
                    if from_type == "current":
                        allowed = from_balance + from_overdraft
                    else:
                        allowed = from_balance
                    if amt > allowed:
                        raise InsufficientFundsError("Insufficient funds for transfer")

                    new_from = (from_balance - amt).quantize(MONEY_QUANT, rounding=ROUND_HALF_UP)
                    new_to = (to_balance + amt).quantize(MONEY_QUANT, rounding=ROUND_HALF_UP)

                    # update balances
                    self.db.execute("UPDATE accounts SET balance = ? WHERE acc_number = ?", (format(new_from), from_acc))
                    self.db.execute("UPDATE accounts SET balance = ? WHERE acc_number = ?", (format(new_to), to_acc))

                    # ledger entries for both accounts
                    tx_id1 = str(uuid.uuid4())
                    tx_id2 = str(uuid.uuid4())
                    ts = now_iso()
                    self.db.execute(
                        "INSERT INTO transactions (tx_id, acc_number, tx_type, amount, timestamp, balance_after, meta) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (tx_id1, from_acc, "transfer_out", format(amt), ts, format(new_from), f"to:{to_acc}")
                    )
                    self.db.execute(
                        "INSERT INTO transactions (tx_id, acc_number, tx_type, amount, timestamp, balance_after, meta) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (tx_id2, to_acc, "transfer_in", format(amt), ts, format(new_to), f"from:{from_acc}")
                    )
        logger.info("Transfer completed: %s -> %s amount=%s", from_acc, to_acc, amt)

    # --------- Querying / Reports ----------
    def get_balance(self, acc_number: int) -> Decimal:
        cur = self.db.execute("SELECT balance FROM accounts WHERE acc_number = ?", (acc_number,))
        row = cur.fetchone()
        if not row:
            raise AccountNotFoundError("Account not found")
        return to_decimal(row[0])

    def get_transactions(self, acc_number: int, limit: int = 100):
        cur = self.db.execute("SELECT tx_id, tx_type, amount, timestamp, balance_after, meta FROM transactions WHERE acc_number = ? ORDER BY timestamp DESC LIMIT ?", (acc_number, limit))
        rows = cur.fetchall()
        return [
            {
                "tx_id": r[0],
                "tx_type": r[1],
                "amount": to_decimal(r[2]),
                "timestamp": r[3],
                "balance_after": to_decimal(r[4]),
                "meta": r[5]
            } for r in rows
        ]

# ---------- Example usage ----------
if __name__ == "__main__":
    # Remove DB for demo to start fresh (comment out in production)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    bank = Bank("MyBank", db_path=DB_PATH)

    # Create accounts
    alice = bank.create_account(1001, "Alice", acc_type="savings", initial_deposit=1000, interest_rate=0.03)
    bob = bank.create_account(1002, "Bob", acc_type="current", initial_deposit=200, overdraft_limit=500)

    print(bank.get_balance(1001))  # 1000.00
    print(bank.get_balance(1002))  # 200.00

    # Deposits and withdrawals
    alice.deposit(250)
    bob.withdraw(600)  # allowed due to overdraft (200 - 600 = -400)

    print("After transactions:")
    print("Alice balance:", bank.get_balance(1001))
    print("Bob balance:", bank.get_balance(1002))

    # Transfer (atomic)
    try:
        bank.transfer(1001, 1002, 300)
    except BankingError as e:
        logger.error("Transfer failed: %s", e)

    print("Final balances:")
    print("Alice balance:", bank.get_balance(1001))
    print("Bob balance:", bank.get_balance(1002))

    # Interest
    acct_alice = bank.get_account(1001)
    if isinstance(acct_alice, SavingsAccount):
        interest = acct_alice.add_interest()
        print("Interest credited to Alice:", interest)

    # Show ledger (recent)
    print("Alice transactions:", bank.get_transactions(1001, limit=10))
    print("Bob transactions:", bank.get_transactions(1002, limit=10))
