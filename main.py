import datetime


class Bank_Account:

    date = datetime.datetime(2020, 1, 9)
    credit = 0
    debit = 0

    def __init__(self, balance):
        self.balance = 0
    
    def deposit(self):
        self.credit = float(input(f'Current balance: {self.balance}.Enter amount to be deposited ')) 
        return self.balance + self.credit
    
    def withdraw(self):
        self.credit = float(input(f'Current balance: {self.balance}.Enter amount to be withdrawn ')) 
        return self.balance - self.credit

bank_account = Bank_Account()

print(bank_account.deposit())