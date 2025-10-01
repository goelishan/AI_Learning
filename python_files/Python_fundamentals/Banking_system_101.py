class InsuffcientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

class AccountNotFoundError(Exception):
     pass

class BankAccount:

    def __init__(self,acc_number,owner,balance=0):
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
    
    def display(self):
        print(f'Account Number - {self.acc_number}')
        print(f'Balance - {self.balance}')



acc=BankAccount('123456','Ishan',5000)
acc.display()
acc.deposit('123456',0)
acc.display()

acc.withdraw('123456',30000)
acc.display()