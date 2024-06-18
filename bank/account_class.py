class Account:
    def __init__(self, name, password, balance):
        self.balance = balance
        self.name = name
        self.password = password
        
    def deposit(self, amount, password):
        if self.password != password:
            print("Sorry, the password is incorrect")
            return None
        
        if amount < 0:
            print("Sorry, you can't deposit such amount, try again")
            return None
        
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount, password):
        if amount < 0:
            print("Wrong amount, it can't be negative")
            return None
        
        if self.password != password:
            print("Incorrect Password")
            return None
            
        if self.balance < amount:
            print("Insuffient Funds")
            return None
        
        self.balance -= amount
        return self.balance
    
    def check_balance(self, password):
        if self.password != password:
            print("Incorrect Password")
            return None
        print(f"You're account balance is {self.balance}")
        return self.balance
    
    def show(self, password):
        if self.password != password:
            print("Incorrect Password")
            return None
        
        print(f"Your account name is: {self.name}")
        print(f"Your account balance is: {self.balance}")
        print(f"Not advisable to display password, but your account password is : {self.password}")