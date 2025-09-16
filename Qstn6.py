#Create a function called divide_numbers that takes two parameters, numerator and denominator
# Use a try block to handle:
#Division by zero (ZeroDivisionError).
#Invalid input types (TypeError).
#The function should return the result of the division if successful, and print an
#appropriate error message for each exception.



def divide_numbers(numerator, denominator):# function with its two parameters
    try:
        result = numerator / denominator  # Try to divide
        return result  # If successful, return the result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")  # Handle division by zero
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")  # Handle wrong types
