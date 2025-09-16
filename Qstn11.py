#What is an API?
# Explain how to make a GET request to an API using the requests library in Python.
#Explain how to connect to a SQLite database using Python. Describe the
#steps involved and the purpose of each step.

#Answers:
# An API is an Abbreviation for Application Programming Interface.
  #it is a set of rules and protocols that allows two Applications to interact with each other. In web development this
    #is usually the interfaces that lets user request data and receive responses

#Steps to get Request using library in python are:
          #1st: Import requests – gives us the ability to send HTTP requests.
          #2nd: Specify API URL – the endpoint you want to request data from.
          #3rd: Send GET request – requests.get(url) asks the server for data.
          #4th: Check status code – ensures the request was successful.
          #5th: Parse response – many APIs return JSON, so we use .json() to convert it into a Python dictionary

#Steps to connecting to an SQL Database using Python;
         #1st: Connect to database – sqlite3.connect("my_database.db") opens (or creates) a database file.
         #2nd: Create a cursor – cursor = connection.cursor() allows execution of SQL commands.
         #3rd: Execute SQL commands – used for creating tables, inserting data, etc.
         #4th: Insert data safely – use placeholders (?, ?) to prevent SQL injection.
         #5th: Commit changes – saves all modifications permanently.
         #6th: Fetch results – fetchall() retrieves rows from the database.
         #7th: Close connection – always close to free up resources.
