#Create a Python script that writes a list of names to a file called names.txt.
# Each name should be on a new line. Then, read the file and print each name to the
#console. Use the with statement to handle file operations and ensure the file is
#properly closed.

# List of names to write to the file
names = ["Rabi", "Winnie", "Pool", "Bear", "Logic"]

# Writing names to the file "names.txt"
with open("names.txt", "w") as file:  # Use the "with" statement to open the file
    for name in names:
        file.write(name + "\n")  # to write each name followed by a newline

#Reading names from the file and printing them
with open("names.txt", "r") as file:  # Open the file in read mode ("r")
    for line in file:
        print(line.strip())  # Print each name, removing the trailing newline
