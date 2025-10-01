# Let’s build a Bank Account class with deposits, withdrawals, and error handling.

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        if amount < 0:
            raise ValueError('Amount cannot be less than 0')
        
        self.balance+=amount
        print(f'{amount} deposited in account, updated balance - {self.balance}')
    

    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError('Insufficient funds')
        
        self.balance-=amount
        print(f'{amount} withdrawn from account, updated balance - {self.balance}')

    
try:
    acc=BankAccount('ishan',5000)
    acc.deposit(400)
    acc.withdraw(60000)
except ValueError:
    print('transaction failed.')
finally:
    print(acc)