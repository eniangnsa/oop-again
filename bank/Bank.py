# create a bank class

from new_account import AbortTransaction, Account

from new_account import AbortTransaction, Account

class Bank:
    def __init__(self, hours, address, phone):
        self.account_dict = {}
        self.next_acct_number = 0
        self.hours = hours
        self.address = address
        self.phone = phone
        
    def ask_for_account_number(self):
        account_number = input('What is your account number?: ')
        
        try:
            account_number = int(account_number)
        except ValueError:
            print("Account Number must be a number")
            
        if account_number not in self.account_dict:
            raise AbortTransaction("Sorry you don't have an account with us")
        
        return account_number
    
    def verify_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("Please enter a number as amount")
        if amount < 0:
            raise AbortTransaction("Sorry, you entered an invalid amount")
        return amount
    
    def get_user_account(self):
        account_number = self.ask_for_account_number()
        account = self.account_dict[account_number]
        return account
        
    def create_account(self, name, amount, password):
        """to create a new account

        Args:
            name (str): name of the account owner
            password (str): password of the user
            amount (int | float): amount to be used in creating the account

        Returns:
            int: user account number 
        """
        account = Account(name, amount, password)
        acct_number = self.next_acct_number
        self.account_dict[acct_number] = account
        # increment to prepare for the next account to be created
        self.next_acct_number += 1
        return acct_number
    
    def open_account(self):
        print("To open an account, we need the following information")
        user_name = input("Please Enter your name: ")
        user_password = input("Please Enter your password: ")
        user_amount = int(input("Please Enter amount to open the account: "))
        account = self.create_account(user_name, user_amount, user_password)
        acct_number = self.next_acct_number
        self.account_dict[acct_number] = account
        self.next_acct_number += 1
        return acct_number
    
    def close(self):
        print("To close your account, enter the following for verification")
        user_name = input("Please Enter your name: ")
        user_password = input("Please Enter your password: ")
        user_acct_number = int(input("Please Enter your account number: "))
        
        print("***First Stage Verification***")
        if user_acct_number not in self.account_dict:
            print("Invalid account details provided")
        
        print("***Second Stage Verification***")    
        if user_name != self.account_dict[user_acct_number].name:
            print("Name mismatch")
        
        print("***checking account balance***")
        if self.account_dict[user_acct_number].get_balance() != 0:
            print(f"You have some money in the account. Your balance is: {self.account_dict[user_acct_number].get_balance()}")
        else:
            del self.account_dict[user_acct_number]
        return "Account Successfully Closed"
    
    def deposit(self):
        print("To make a deposit, please provide the following information")
        user_amount = int(input("Please Enter the amount you want to deposit: "))
        print("***Amount Verification***")
        user_amount = self.verify_amount(user_amount)
        user_acct_number = self.get_user_account()
        user_password = input("Please Enter your password: ")
        print("***Password Verification***")
        if user_password != self.account_dict[user_acct_number].password:
            print("Invalid Password Provided")
        
        new_balance = self.account_dict[user_acct_number].deposit(user_amount)
        print(f"Your new balance is: {new_balance}")
    
    def withdraw(self):
        print("Withdraw")
        user_acct_number = self.get_user_account()
        user_password = input("Please enter your password: ")
        user_amount = int(input("How much do you want to withdraw: "))
        user_amount = self.verify_amount(user_amount)
        # get account object from account_dict
        acct_object = self.account_dict[user_acct_number]
        # verify if the password is correct
        if user_password != acct_object.password:
            print("Incorrect Password was entered")
        # verify if the amount is a valid one
        if user_amount > acct_object.get_balance():
            print("Insufficient Funds")
        new_balance = acct_object.withdraw(user_amount)
        print(f"Withdraw Successful. Here's your new balance: {new_balance}")
        
    def show(self):
        user_acct_number = int(input("Please Enter account number: "))
        user_password = input("Please Enter your password: ")
        
        # check if account exists
        if user_acct_number in self.account_dict:
            if user_password != self.account_dict[user_acct_number].password:
                print("Incorrect Password")
            acct_object = self.account_dict[user_acct_number]
            acct_object.show()
        else:
            print("Sorry, This account does not exist")
