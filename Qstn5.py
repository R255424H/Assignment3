#Write a Python program that uses a lambda function and the map function to
#convert a list of temperatures in Celsius to Fahrenheit.
#The formula for conversion is F = C * 9/5 + 32. Include a sample list of Celsius temperatures and print the
#converted list.

# Sample list of temperatures in Celsius
celsius_temps = [0, 20, 30, 40, 100]

# Use map() with a lambda function to convert each Celsius value to Fahrenheit
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

# Print the converted list
print("Temperatures in Celsius:", celsius_temps)
print("Converted to Fahrenheit:", fahrenheit_temps)
