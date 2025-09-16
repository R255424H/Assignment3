# Write a program that handles user input for a number.
# Use a try block to catch any ValueError exceptions that may occur if the user inputs an invalid number.
# Print an error message and prompt the user to enter a valid number again.

while True: #this loop repeats condition until valid input
    try: #this is where the program accepts user input and stores number if float (integers with a decimal)
        user_input = input("Enter a number: ")
        number = float(user_input)
        print(f"You entered a valid number: {number}")
        break
        #the exception  where the user inputs an invalid value such as a string the ValueError function gives message
    except ValueError:
        print("Invalid input. Please enter a valid number.")
