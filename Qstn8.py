#Write a Python program that uses the random module to generate a list of 10
#random integers between 1 and 100. Then, calculate and print the average of the
#generated numbers. Use appropriate functions to achieve this.

import random   # Import the random module

# Function to generate random numbers
def generate_random_numbers(count, start=1, end=100):
    """
    Generates a list of 'count' random integers between 'start' and 'end'.
    """
    numbers = [random.randint(start, end) for _ in range(count)]
    return numbers

# Function to calculate average
def calculate_average(numbers):
    """
    Takes a list of numbers and returns their average.
    """
    return sum(numbers) / len(numbers)


# Main program
def main():
    numbers = generate_random_numbers(10, 1, 100)  # Step 1: Generate 10 random integers
    average = calculate_average(numbers)           # Step 2: Calculate their average

    # Step 3: Print results
    print("Generated numbers:", numbers)
    print("Average:", average)


# Run the program
if __name__ == "__main__":
    main()
