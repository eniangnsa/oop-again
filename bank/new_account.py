# Account Class
# Errors indicated by the 'raise' statement

# Define a custom exception
class AbortTransaction(Exception):
    '''
    raise this exception to abort a bank transaction
    '''
    pass

class Account:
    def __init__(self, name, balance, password):
        self.nanme = name
        self.balance = self.validate_amount(balance)
        self.password = password
        
    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction("Amount must be positive")
        return amount
    
    def check_password(self, password):
        if self.password != password:
            raise AbortTransaction("Incorrect Password for this account")
    
    def deposit(self, amount):
        amount = self.validate_amount(amount)
        self.balance += amount
        return self.balance
    
    def balance(self):
        return self.balance
    
    def withdraw(self, amount):
        amount = self.validate_amount(amount)
        if amount > self.balance:
            raise AbortTransaction("Insuffient funds")
        self.balance -= amount
        return self.balance
    
    def show(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Password: {self.password}")
        