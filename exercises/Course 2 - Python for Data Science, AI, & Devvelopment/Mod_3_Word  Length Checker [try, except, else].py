# Exercise: Word Length Checker
# Write a program that asks the user to enter a word.
# Then ask the user to enter a number.
#
# The program should:
# 1. Try to convert the number input into an integer.
# 2. If the input is not a valid number, handle the error with try-except.
# 3. If it *is* a number (no error), use 'else' to check:
#    - If the number is equal to the word length, print "Correct!"
#    - Otherwise, print the actual length of the word.
#
# Bonus: Keep asking until the user types "q" to quit.

while True:

    word = input("Enter a word: ")
    if word.lower() == "q":
        break

    while True:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        else:
            if num == len(word):
                print("Correct!")
                break
            else:
                print(f"The number of letters is {len(word)}")
                break
