# main file version 4
# This version makes use of the Bank Class

from Bank import Bank

# Create a bank object from the Bank class

Zenith_Bank = Bank()

# create two account for Zenith Bank
kirill_acct_number = Zenith_Bank.create_account("Kirill", "kirill@siberia",10_000)
print(f"New Account opened. name is : {Zenith_Bank.account_dict[kirill_acct_number].name} and account number is:  {kirill_acct_number}")

david_acct_number  = Zenith_Bank.create_account("David", "david@siberia", 20_000)
print(f"New Account opened. name is : {Zenith_Bank.account_dict[david_acct_number].name} and account number is:  {david_acct_number}")


while True:
    print("Hello and Welcome to our bank")
    print("Please follow the instructions and enter just a letter to tell us the operation you want.")
    print("To open an account, press o")
    print("To close an account, press c")
    print("To deposit money, press d")
    print("To withdraw money, press w")
    print("To show account details, press s")
    print("To check balance, press b")
    print("To quit, press q")
    
    print(Zenith_Bank.account_dict)
    action = input("What do you want to do ? ")
    
    if action == "d":
        Zenith_Bank.deposit()
    
    elif action == "w":
        Zenith_Bank.withdraw()
    
    elif action == "o":
        Zenith_Bank.open_account()
    
    elif action == "c":
        Zenith_Bank.close()
        
    elif action == "s":
        Zenith_Bank.show()
        
    elif action == "q":
        break
    
    elif action == 'b':
        Zenith_Bank.balance()
    else:
        print("Sorry, you entered an invalid input")
    break
        
    
print("E don do")