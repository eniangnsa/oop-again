# Test program using accounts
# Version 3 using dict to store individual accounts open

"""
one of the major drawback of using a list to store our  different account is the problem that arises when a user deletes an account. The indexes will be updated and the other users will take 
a new index. so this problem can be solved by a dictionary. This is because we're now working with key/value pairs. if a user deletes an account, only that account is affected.
others remain the same. 
"""

# import the account class
from account_class import Account

# create an account dictionary
account_dict = {}
next_account_number = 0

# create an account for two users
account = Account("Vlad", "vlad@siberia", 20_000)
vlad_account_number = next_account_number
account_dict[vlad_account_number] = account
print(f"Vlad's Account Number is: {vlad_account_number}")
next_account_number += 1

account = Account("Sasha", "sasha@siberia", 2000_000)
sasha_account_number = next_account_number
account_dict[sasha_account_number] = account
print(f"Sasha's account number is: {sasha_account_number}")
next_account_number += 1

# print vlad's account details
account_dict[vlad_account_number].show(account_dict[vlad_account_number].password)

# print sasha's account details
account_dict[sasha_account_number].show(account_dict[sasha_account_number].password)

# next let's create a dynamic interface that allows users to create an account and  carry some operations on the account
user_name = input("Please Enter your name: ")
password = input("Please Enter  a password for the account: ")
balance = int(input("Enter an amount for the account: "))

account  = Account(user_name, password, balance)
next_account_number = next_account_number
account_dict[next_account_number] = account
print(f"The account number for the new account is: {next_account_number}")
next_account_number += 1

# create the interactive part

while True:
    print("Hello, Welcome. Below are a few actions you can do")
    print("To create a new account, enter 'new' : ")
    print("To check your balance, enter 'b' ")
    print("To deposit, enter 'd' ")
    print("To withdraw money, press 'w' ")
    print("To show account details, enter 's' ")
    print("To quit, enter 'q' ")
    
    operation = input("What operation do you want to perform? ")
    if operation == 'new':
        print("To create a new account, please enter the following details ")
        new_name = input("Please Enter your name: ")
        new_balance = int(input("Please Enter your amount to be deposited: "))
        new_password = input("Please Enter your Password: ")
        
        # create the account
        new_account = Account(new_name, new_password, new_balance)
        next_account_number = next_account_number
        account_dict[next_account_number] = new_account
        print(f"Your new account has been created. here's your account number: {next_account_number}")
        next_account_number += 1
        
    elif operation == 'b':
        account_number  = int(input("Please Enter account number: "))
        account_password = input("Please enter your password: ")
        if account_number in account_dict:
            if account_password != account_dict[account_number].password:
                print("Invalid Password")
            print(f"Your balance is: {account_dict[account_number].balance}")
            
    elif operation == 'd':
        account_number  = int(input("Please Enter account number: "))
        account_password = input("Please enter your password: ")
        account_amount = int(input("Enter amount to deposit: "))
        if account_number in account_dict:
            if account_password != account_dict[account_number].password:
                print("Invalid Password")
            if account_amount < 0:
                print("Sorry invalid amount entered")
            account_dict[account_number].balance += account_amount
            print(f"Your new balance is: {account_dict[account_number].balance}")
              
    elif operation == 'w':
        account_number  = int(input("Please Enter account number: "))
        account_password = input("Please enter your password: ")
        account_amount = int(input("Enter the amount for withdrawal: "))
        if account_number in account_dict:
            if account_password != account_dict[account_number].password:
                print("Invalid Password")
            if account_amount < 0:
                print("Sorry, you entered an invalid amount")
            if account_dict[account_number].balance < account_amount:
                print("Sorry, insufficient funds.")
            account_dict[account_number].balance -= account_amount
            print(f"Your new balance is: {account_dict[account_number].balance}")
            
    elif operation == 's':
        account_number  = int(input("Please Enter account number: "))
        account_password = input("Please enter your password: ")
        if account_number in account_dict:
            if account_password != account_dict[account_number].password:
                print("Invalid Password")
                
            print(f"Here is your account details: {account_dict[account_number].show(account_password)}")
            
    elif operation == 'q':
        break
        
    else:
        print("Sorry, you entered an invalid command")
    break
    
print("Done!!")

    