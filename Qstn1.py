#Write a Python function named classify_number that takes an integer as input and
# returns Positive if the number is greater than zero
#  return Negative if the number is less than zero.
# Zero if the number is zero.

#Use a while loop to repeatedly prompt the user for a number until they enter a valid integer.

def classify_number(): #as python function

    while True: #loop to prompt user to enter number
        try:# to check the value type if not Integer
            number = int(input("Enter a number: ")) #number to store prompted input
            # If_Statement to condition the input
            if number > 0:
                return "Positive"
            elif number < 0:
                return "Negative"
            else:
                return "Zero"

        except ValueError:
            print("That is not an integer", "Try again")

print(classify_number())