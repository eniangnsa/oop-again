# NO - OOP
# BANK ACCOUNT DEMO 2
# SINGLE ACCOUNT

# Initialize some global variable
account_name = ''
account_balance = 0
account_password = ''

# define functions that will take care of some common actions

# Create account function
def new_account(name, balance, password):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password
    
# Function to show account details
def show():
    global account_name, account_balance, account_password
    print(f"The Account Name is : {account_name}")
    print(f"The Account password is : {account_password}")
    print(f"The Account Balance is : {account_balance}")
    
# get balance
def get_balance(password):
    global account_balance, account_password, account_name
    if password != account_password:
        print("Incorrect Password")
        return None
    else:
        return account_balance
    
# deposit money
def deposit(amount, password):
    global account_name, account_password, account_balance
    print("Deposit into account ")
    if password != account_password:
        print("Incorrect Password")
    elif amount < 0:
        print("Sorry, you entered an invalid amount")
        return None
        
    else:
        account_balance += amount
        print("Amount successfully deposited")
        return account_balance
    
# Withdraw money
def withdraw(amount, password):
    global account_balance, account_name, account_password
    # check if the amount is less than the balance
    if amount < account_balance:
        print("Insufficient Funds")
        return None
    elif password != account_password:
        print("Incorrect Password")
        return None
    else:
        account_balance -= amount
        print("Amount successfully withdrawn")
        return account_balance
    
# Create a new account
new_account(name="Kirill", balance=100, password='kirill@sbai')

while True:
    print()
    print("Press b to check account balance")
    print("Press d to deposit to the account")
    print("Press w to withdraw from the account")
    print("Press s to show account details")
    print("Press q to quit")
    print()
    
    # create an action variable
    action = input("What do you want to do ? : ")
    action = action.casefold()
    action = action[0]
    
    if action == 'b':
        input_password = input("Please enter your password : ")
        the_balance = get_balance(input_password)
        if the_balance is not None:
            print(f"Your Balance is : {the_balance}")
    
    elif action == 'd':
        amount = input("Please Enter your Amount : ")
        amount = int(amount)
        password = input("Please enter your password : ")
        
        deposit = deposit(amount, password)
        if deposit is not None:
            print(f"The amount has been deposited, new balance : {account_balance}")
    
    elif action == 's':
        show()
    
    else:
        break
    
print("Transaction Done")
