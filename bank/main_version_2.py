# Test program using accounts
# Version 2 using list to store individual accounts open

# import the code from the account_class.py file
from account_class import Account

# create an empty list to start with
account_list = []

# create two accounts and append them to the list
account = Account("Kirill", "kirill@siberia", 10_000)
account_list.append(account)
print(f"The user whose name is : {account.name} just created an account")

# create another account
account = Account("danil", "danil@siberia", 200_000)
account_list.append(account)
print(f"Another user whose name is : {account.name} just created an account")

# Also i can create yet another account with  user input
user_name = input("Please enter your name: ")
user_balance = int(input("Please enter your starting amount: "))
user_password = input("Enter  your password:  ")

# create an account using the user input data
account = Account(user_name, user_password, user_password)
account_list.append(account)
print(f"The user whose name is : {account.name} just created an account")
account.show(account.password)