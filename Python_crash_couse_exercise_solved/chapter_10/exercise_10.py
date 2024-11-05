# 10.1 Learning Python

from pathlib import Path

# Specify the file path
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\learning_python.txt')

# Read the entire content of the file
content = path.read_text()

# Print the complete content in one go
print("Content read in one go:\n")
print(content, "\n")

# Split the content into lines and store them in a list
line_by_line = content.splitlines()
list_of_content = []

# Append each line to a list
for line in line_by_line:
    list_of_content.append(line)

# Print each line individually by iterating over the list
print("Content printed line-by-line from list:\n")
for line in list_of_content:
    print(line)
print()

#########################################################

# 10.2 Learning C

from pathlib import Path

# Specify the file path
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\learning_python.txt')

# Read the entire content of the file
content = path.read_text()

# Replace every occurrence of 'Python' with 'C' in the content
new_content = content.replace('Python', 'C')

# Print each line after replacing 'Python' with 'C'
print("Modified content with 'Python' replaced by 'C':\n")
print(new_content , '\n')

########################################################

# 10.3 Simpler Code

from pathlib import Path

# Specify the file path
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\learning_python.txt')

# Read the entire content of the file
content = path.read_text()

# Print each line individually by iterating over the list
print("Content printed line-by-line :\n")
for line in content.splitlines():
    print(line)
print()

###########################################################

# 10.4 Guest:

from pathlib import Path

# Prompt the user for their name
name = input('What is your name? : ')

# Define the path for the file to save the name
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\guest.txt')

# Write the user's name to the file
path.write_text(name.title())

# Read the content of the file to confirm it was saved correctly
content = path.read_text()

# Print the content read from the file
print(f"Name saved in guest.txt: {content} \n")

##################################

# 10.5 Guest Book

from pathlib import Path

# Define the path for the file where names will be stored
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\guest_book.txt')

while True:
    name = input('What is your name? (Enter "quit" to stop): : ')

    # Check if the user wants to exit
    if name.lower() == 'quit':
        print('Exiting and saving all names to guest_book.txt.')
        break

    # Append the name to the file on a new line
    with path.open(mode='a') as file:
        file.write(name.title() + '\n')

    # Confirm that the name was saved
    print(f"Hello, {name.title()}! Your name has been added to the guest book. \n")

###################################################

# 10.6 & 10.7 Addition & Addition Calculator

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue  # This allows the user to try again if they enter non-integer input
    else:
        # Calculate and display the result if inputs are valid
        addition = num1 + num2
        print(f"The sum of {num1} and {num2} is: {addition} \n")
        break  # Exit the loop once successful input has been provided

#################################################

# 10.8 Cats and Dogs

from pathlib import Path

# List of files to read
files = ['cats.txt', 'dogs.txt']

for file in files:
    try:
        # Define the path for each file
        path = Path(f"D:/AI in 2024/PIAIC/quarter 1/GitHub/PIAIC-Q1/Python_crash_couse_exercise_solved/chapter_10/{file}")
        
        # Read and display content of each file
        content = path.read_text()
        print(f"Contents of {file}:\n{content}\n")

    except FileNotFoundError:
        print(f"Sorry, the file '{file}' was not found.\n")

####################################################

# 10.9 silent Cats and Dogs

from pathlib import Path

# List of files to read
files = ['cats.txt', 'dogs.txt']

for file in files:
    try:
        # Define the path for each file
        path = Path(f"D:/AI in 2024/PIAIC/quarter 1/GitHub/PIAIC-Q1/Python_crash_couse_exercise_solved/chapter_10/{file}")
        
        # Read and display content of each file
        content = path.read_text()
        print(f"Contents of {file}:\n{content}\n")

    except FileNotFoundError:
        pass

###########################################################

# 10.11 Favorite Number

from pathlib import Path
import json

# Prompt the user for their favorite number
num = input('Enter your favorite number: ')

# Define the file path to save the number
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\favorite_number.json')

# Save the number to a JSON file
content = json.dumps(num)
path.write_text(content)

print("Your favorite number has been saved!")

# ************************************

from pathlib import Path
import json

# Define the file path where the number is stored
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\favorite_number.json')

# Read the content from the JSON file
content = path.read_text()
favorite_number = json.loads(content)
print(f"I know your favorite number! It’s {favorite_number}. \n")

#############################################################################################

# 10.12 Favorite Number Remembered

from pathlib import Path
import json

# Define the file path for storing the favorite number
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\favorite_number.json')

# Check if the favorite number file already exists
if path.exists():
    # Read the favorite number from the file
    content = path.read_text()
    favorite_number = json.loads(content)
    print(f"I know your favorite number! It’s {favorite_number}. \n")
else:
    # Prompt the user for their favorite number
    num = input("Enter your favorite number: ")

    # Save the number to the JSON file
    content = json.dumps(num)
    path.write_text(content)
    
    print("Your favorite number has been saved!")

########################################################

# 10.13 User Dictionary

from pathlib import Path
import json

# Define the path to the file where user information is stored
path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\user_data.json')

# Check if user information already exists
if path.exists():
    # Read the existing data and load it as a dictionary
    content = path.read_text()
    user_data = json.loads(content)
    
    # Display a summary of the stored information
    print("Welcome back! Here’s what I remember about you:")
    print(f"Name: {user_data['Name']}")
    print(f"Education: {user_data['Education']}")
    print(f"Age: {user_data['Age']} \n")

else:
    # Collect new user information
    user_data = {}
    user_data['Name'] = input('Enter your name: ').title()
    user_data['Education'] = input('Enter your education: ').title()
    user_data['Age'] = int(input('Enter your age: '))

    # Save the user information to the JSON file
    content = json.dumps(user_data)
    path.write_text(content)

    print("\nThank you! Your information has been saved. \n")

########################################################################

# 10.14 Verify User

from pathlib import Path
import json

def get_stored_username(path):
    """Retrieve the stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None

def get_new_username(path):
    """Prompt for a new username and save it to the file."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username))  # Save the username to JSON format
    return username

def greet_user():
    """Greet the user by name, checking if it's the correct user."""
    # Path to the file where username is stored
    path = Path(r'D:\AI in 2024\PIAIC\quarter 1\GitHub\PIAIC-Q1\Python_crash_couse_exercise_solved\chapter_10\user_name.json')
    
    # Get the stored username if available
    username = get_stored_username(path)
    
    # Check if a username was found
    if username:
        checker = input(f"Is this your name: '{username}'? (Y for Yes, N for No): ")
        if checker.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"Your new name has been saved. Welcome, {username}!")
    else:
        # If no username was stored, prompt for a new one
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

# Run the greeting function
greet_user()