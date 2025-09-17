# Exercise: Safe Data Retriever
# You have a small "database" of user accounts with balances:

accounts = {
    "alice": 500,
    "bob": 300,
    "charlie": 0
}

# Write a program that:
# 1. Asks the user for a username.
# 2. Asks the user to enter an amount to withdraw.
# 3. Uses try-except-else to handle the following:
#    - KeyError: If the username does not exist in the accounts.
#    - ValueError: If the withdrawal amount is not a number.
#    - ZeroDivisionError (just for practice!):
#       if you try to divide by the amount entered (simulate some operation)
# 4. If no exceptions occur, subtract the withdrawal from the account and print the new balance.
# 5. Keep asking until the user types "q" as the username.

while True:
    user = input("Enter username (or 'q' to quit): ")
    if user.lower() == "q":
        break

    try:
        accounts[user]
    except KeyError:
        print("Enter a valid user.")
        continue

    num = input("Enter an amount to withdraw: ")
    try:
        num = int(num)
        if num < 0:
            print("Enter a positive amount.")
            continue
    except ValueError:
        print("Enter a valid number.")
        continue

    if accounts[user] < num:
        print(f"Unable to withdraw. Balance is {accounts[user]}")
    else:
        accounts[user] -= num
        print(f"New balance is {accounts[user]}")
