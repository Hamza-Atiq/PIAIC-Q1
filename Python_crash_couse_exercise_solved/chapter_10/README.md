
# Chapter 10: File Handling and User Data Management in Python

This chapter covers practical exercises in reading, writing, and managing files using Python's `pathlib` and `json` libraries. Through these exercises, you will learn how to work with files, prompt user input, and manage persistent user data.

---

## Table of Contents

1. [Exercise 10.1: Learning Python](#exercise-101-learning-python)
2. [Exercise 10.2: Learning C](#exercise-102-learning-c)
3. [Exercise 10.3: Simpler Code](#exercise-103-simpler-code)
4. [Exercise 10.4: Guest](#exercise-104-guest)
5. [Exercise 10.5: Guest Book](#exercise-105-guest-book)
6. [Exercise 10.6 & 10.7: Addition & Addition Calculator](#exercise-106-107-addition--addition-calculator)
7. [Exercise 10.8: Cats and Dogs](#exercise-108-cats-and-dogs)
8. [Exercise 10.9: Silent Cats and Dogs](#exercise-109-silent-cats-and-dogs)
9. [Exercise 10.11: Favorite Number](#exercise-1011-favorite-number)
10. [Exercise 10.12: Favorite Number Remembered](#exercise-1012-favorite-number-remembered)
11. [Exercise 10.13: User Dictionary](#exercise-1013-user-dictionary)
12. [Exercise 10.14: Verify User](#exercise-1014-verify-user)

---

### Exercise 10.1: Learning Python

In this exercise, we read the contents of a file and display them in three ways: all at once, line-by-line by storing each line in a list, and by iterating over the list.

```python
from pathlib import Path

# Specify the file path
path = Path(r'D:\path\to\learning_python.txt')

# Read the entire content of the file
content = path.read_text()

# Print the content in one go
print("Content read in one go:\n")
print(content, "\n")

# Read the content line by line and store in a list
line_by_line = content.splitlines()

# Print each line individually by iterating over the list
print("Content printed line-by-line from list:\n")
for line in line_by_line:
    print(line)
```

---

### Exercise 10.2: Learning C

This exercise modifies the content of a file by replacing every occurrence of the word “Python” with “C.” This showcases Python’s `replace` method.

```python
from pathlib import Path

path = Path(r'D:\path\to\learning_python.txt')
content = path.read_text()

# Replace every occurrence of 'Python' with 'C'
new_content = content.replace('Python', 'C')
print("Modified content with 'Python' replaced by 'C':\n")
print(new_content , '\n')
```

---

### Exercise 10.3: Simpler Code

This exercise simplifies reading a file by using a direct loop to print each line.

```python
from pathlib import Path

path = Path(r'D:\path\to\learning_python.txt')
content = path.read_text()

# Print each line
print("Content printed line-by-line:\n")
for line in content.splitlines():
    print(line)
```

---

### Exercise 10.4: Guest

Here, we prompt the user for their name and save it to a file named `guest.txt`.

```python
from pathlib import Path

name = input('What is your name? : ')
path = Path(r'D:\path\to\guest.txt')

# Write the name to the file
path.write_text(name.title())

print(f"Name saved in guest.txt: {name.title()}")
```

---

### Exercise 10.5: Guest Book

This code repeatedly prompts users to enter their names until they type "quit". Each name is appended to `guest_book.txt`.

```python
from pathlib import Path

path = Path(r'D:\path\to\guest_book.txt')

while True:
    name = input('What is your name? (Enter "quit" to stop): ')
    if name.lower() == 'quit':
        break
    with path.open(mode='a') as file:
        file.write(name.title() + '\n')
    print(f"Hello, {name.title()}! Your name has been added to the guest book.")
```

---

### Exercise 10.6 & 10.7: Addition & Addition Calculator

This exercise includes exception handling to manage non-integer inputs and calculates the sum of two numbers.

```python
while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue
    else:
        addition = num1 + num2
        print(f"The sum of {num1} and {num2} is: {addition}")
        break
```

---

### Exercise 10.8: Cats and Dogs

This code reads and prints the content of two files, handling potential file-not-found errors.

```python
from pathlib import Path

files = ['cats.txt', 'dogs.txt']
for file in files:
    path = Path(f"D:/path/to/{file}")
    try:
        content = path.read_text()
        print(f"Contents of {file}:\n{content}\n")
    except FileNotFoundError:
        print(f"Sorry, the file '{file}' was not found.")
```

---

### Exercise 10.9: Silent Cats and Dogs

Similar to the previous exercise, but silently ignores file-not-found errors.

```python
from pathlib import Path

files = ['cats.txt', 'dogs.txt']
for file in files:
    path = Path(f"D:/path/to/{file}")
    try:
        content = path.read_text()
        print(f"Contents of {file}:\n{content}\n")
    except FileNotFoundError:
        pass
```

---

### Exercise 10.11: Favorite Number

In this exercise, the user’s favorite number is stored in a JSON file.

```python
from pathlib import Path
import json

num = input('Enter your favorite number: ')
path = Path(r'D:\path\to\favorite_number.json')
content = json.dumps(num)
path.write_text(content)
print("Your favorite number has been saved!")
```

---

### Exercise 10.12: Favorite Number Remembered

This exercise retrieves and displays a stored favorite number if it exists.

```python
from pathlib import Path
import json

path = Path(r'D:\path\to\favorite_number.json')
if path.exists():
    favorite_number = json.loads(path.read_text())
    print(f"I know your favorite number! It’s {favorite_number}.")
else:
    num = input("Enter your favorite number: ")
    path.write_text(json.dumps(num))
    print("Your favorite number has been saved!")
```

---

### Exercise 10.13: User Dictionary

This code collects and stores user information in a JSON file, or displays it if it already exists.

```python
from pathlib import Path
import json

path = Path(r'D:\path\to\user_data.json')
if path.exists():
    user_data = json.loads(path.read_text())
    print("Welcome back! Here’s what I remember about you:")
    print(f"Name: {user_data['Name']}")
    print(f"Education: {user_data['Education']}")
    print(f"Age: {user_data['Age']}")
else:
    user_data = {
        'Name': input('Enter your name: ').title(),
        'Education': input('Enter your education: ').title(),
        'Age': int(input('Enter your age: '))
    }
    path.write_text(json.dumps(user_data))
    print("Your information has been saved.")
```

---

### Exercise 10.14: Verify User

This code verifies if a stored username is correct. If not, it allows the user to enter a new one.

```python
from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        return json.loads(path.read_text())
    return None

def get_new_username(path):
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    path = Path(r'D:\path\to\user_name.json')
    username = get_stored_username(path)
    if username:
        checker = input(f"Is this your name: '{username}'? (Y for Yes, N for No): ")
        if checker.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"Your new name has been saved. Welcome, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

--- 

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.

