#Define a custom exception class called NegativeNumberError that inherits from the
#built-in Exception class. Write a function check_positive that raises this exception if
#a given number is negative.
#Demonstrate the use of this function in a try block.

# 1. Define a custom exception class
class NegativeNumberError(Exception):
    """Raised when a negative number is passed to check_positive()."""
    pass


# 2. Define the function that raises the exception
def check_positive(number):
    """Check if number is positive. Raise NegativeNumberError if negative."""
    if number < 0:
        raise NegativeNumberError(f"Negative number not allowed: {number}")
    return number


# 3. Demonstration using try/except
try:
    value = -10  # You can change this number to test
    print("Checking number:", value)
    result = check_positive(value)
    print("Number is valid:", result)

except NegativeNumberError as e:
    print("Caught an exception:", e)