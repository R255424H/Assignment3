def calculate_average(*args):
    #below is our, docstring, this is resembled by the triple quotes
    """
    This function takes a variable number of arguments and calculates their average.
    Parameters:
        *args (int, float): A variable number of numeric values (can be integers or floats).
    Returns:
        float: The average of the provided numbers.
    Raises:
        ValueError: If no numbers are provided.
    """

    # the If_Statement checks if any arguments are provided (the *args) if not it prompts the error message
    if len(args) == 0: #the len function then counts how many variables present
        raise ValueError("At least one number must be provided to calculate the average.")

    # calculate the sum of all numbers
    total = sum(args)

    # calculate the average by dividing the total by the number of arguments
    average = total / len(args)

    return average
