from account_class import Account

kirill_account = Account("Kirill", "Kirill@siberia", 10_000)
print("Created an account for Kirill")

dasha_account = Account("Dasha", "dasha@siberia", 100_000)
print("Created an account for Dasha")

# let's see the details
kirill_account.show("Kirill@siberia")
dasha_account.show("dasha@siberia")
print()


# Let's call some methods on the objects
kirill_account.deposit(10_000, "Kirill@siberia")
dasha_account.withdraw(10_000, "dasha@siberia")

# show new account details
kirill_account.show("Kirill@siberia")
print()
dasha_account.show("dasha@siberia")

# Let's extend this and make it more interactive
print()
user_name = input("Please Enter name for your user account: ")
user_balance = int(input("how much do you want to open the account with: "))
user_password = input("Please Enter your password : ")

# Create a new object
new_account = Account(user_name, user_password, user_balance)

# Show initial details of the 
new_account.show(user_password)

# deposit 100 into the new account
new_account.deposit(100, user_password)

