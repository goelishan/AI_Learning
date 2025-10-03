class InsuffcientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

class AccountNotFoundError(Exception):
     pass

class BankAccount:

    def __init__(self,acc_number,owner,balance:float):
        self.acc_number=acc_number
        self.owner=owner
        self.balance=balance
    
    def deposit(self,acc_number,amount):

        try:
            if self.acc_number != acc_number:
                raise AccountNotFoundError('Invalid account number')
            if amount<=0:
                raise InvalidTransactionError('Deposit Amount must be greater than 0.')
            else:
                self.balance+=amount
                print(f'\nAccount Number: {self.acc_number}\nAmount deposited: {amount}\nUpdated balance:{self.balance}')
            
            
        except AccountNotFoundError as e:
            print(f"Account Error: {e}")
        except InvalidTransactionError as e:
            print(f"Deposit Error: {e}")
        finally:
            print("Deposit attempt finished.\n")
        
    def withdraw(self,acc_number,amount):

        try:
            if self.acc_number!=acc_number:
                raise AccountNotFoundError('Invalid account number')
            if amount>self.balance:
                raise InsuffcientFundsError(f'Insufficient funds!\n{amount} cannot be withdrawn from account')
            else:
                self.balance-=amount
                print(f'For {self.acc_number} -> Amount withdraw -> {amount}')
        except AccountNotFoundError as e:
            print(f'Account Error: {e}')
        except InsuffcientFundsError as e:
            print(f'Withdrawal Error: {e}')
        finally:
            print('Withdhrawal attempt finished\n')
    
    # def transfer(self,target_acc:'BankAccount',amount:float):
    #     self.withdraw(amount)
        
    
    def display(self):
        print(f'Account Number - {self.acc_number}')
        print(f'Balance - {self.balance}')

# -------------------------Specialized accounts------------------------------

class SavingsAccount(BankAccount):

    def __init__(self,acc_number:int,owner:str,balance:float,interest_rate:float):
        super().__init__(acc_number,owner,balance)
        self.interest_rate=interest_rate
    
    def apply_interest(self):

        interest=self.balance*self.interest_rate
        self.balance+=interest
        return interest
    
class CurrentAccount(BankAccount):

    def __init__(self,acc_number:int,owner:str,balance:float,overdraft:float):
        super().__init__(acc_number,owner,balance)
        self.overdraft=overdraft
    
    def withdraw_overdraft(self,amount):

        if amount<0:
            raise InvalidTransactionError('Withdraw amount should be greater than 0.')
        if amount>self.balance+self.overdraft:
            raise InsuffcientFundsError('Exceeds overdraft limit.')

        self.balance-=amount

# ----------------------------Bank Class---------------------------------------------

class Bank:
    def __init__(self,name:str):
        self.name=name
        self.accounts: dict[int,BankAccount]={}
    
    def add_account(self,account:BankAccount):
        if account.acc_number in self.accounts:
            raise InvalidTransactionError('Account already exists.')
        self.accounts[account.acc_number]=account

    def get_acount(self,acc_number:int)->BankAccount:
        if acc_number not in self.accounts:
            raise InvalidTransactionError('Account not found.')
        return self.accounts[acc_number]
    
    def transfer(self,from_acc:int,to_acc:int,amount:float):
        source=self.get_acount(from_acc)
        target=self.get_acount(to_acc)
        # source.transfer(target,source)



# --------------------------Calling function-----------------------------------------------------

bank = Bank("State Bank")

# Create accounts
a1 = SavingsAccount(101, "Alice", 1000, interest_rate=0.05)
a2 = CurrentAccount(102, "Bob", 500, overdraft=200)

bank.add_account(a1)
bank.add_account(a2)

# Transactions
a1.deposit(101,200)
a1.apply_interest()
# a2.withdraw_overdraft(800)   # overdraft used
# bank.transfer(101, 102, 300)

print(a1)
print(a2)
