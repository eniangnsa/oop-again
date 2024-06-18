# Non - OOP
# Bank Account demo
# Single Account

account_name = "Kirill"
account_balance = 100
account_password = "kirill@sbai"

while True:
    print()
    print("Press b to get the Account Balance")
    print("Press d to make deposit")
    print("Press w to make withdrawals")
    print("Press s to show account")
    print("Press q to quit")
    print()
    
    action = input("What do you want to do ?: ")
    action = action.casefold()
    action = action[0] 
    print()
    
    if action == 'b':
        print("Get Balance")
        password = input("Please enter your password: ")
        
        if password != account_password:
            print("Sorry, the password is incorrect")
            
        else:
            print(f"Here's your Balance: {account_balance}")
            
    elif action == 'd':
        print("Make deposit")
        amount = input("Please enter the amount here : ")
        amount = int(amount) # change it to an int
        password = input("Please enter your password : ")
        
        if amount < 0:
            print("Sorry you can't make deposits of negative figures")
            
        elif password != account_password:
            print("Incorrect Password")
            
        else:
            account_balance += amount
            print("The money has been deposited successfully")
        
    elif action == "w":
        print("Make Withdrawals")
        password = input("Please enter your password : ")
        amount = input("How much do you want to withdraw? ")
        amount = int(amount)
        
        if password != account_password:
            print("Incorrect Password")
            
        elif amount  > account_balance:
            print("Sorry, you can't withdraw what you don't have")
            
        else:
            account_balance -= amount
            print(f"You have withdrawn {amount} successfully")
    
    elif action == "s":
        print("Show account details")
        print(f"The account name is : {account_name}")
        print(f"The account balance is : {account_balance}")
        print(f"Account password is : {account_password}")
    
    elif action == 'q':
        break
print("Thank you for banking with us :) ")
    