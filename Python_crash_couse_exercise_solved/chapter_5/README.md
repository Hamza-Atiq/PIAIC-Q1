
# Python Exercises - Book Chapter 5

Welcome to my repository for Python exercises from Chapter 5. This chapter focuses on conditional statements, an essential concept in programming. By practicing these exercises, you'll learn how to make decisions in your code, use comparison operators, and control program flow using conditional logic.

## Table of Contents
1. [5.1 Conditional Tests](#51-conditional-tests)
2. [5.2 More Conditional Tests](#52-more-conditional-tests)
3. [5.3 - 5.5 Alien Colors 1, 2, & 3](#53---55-alien-colors-1-2--3)
4. [5.6 Stages of Life](#56-stages-of-life)
5. [5.7 Favorite Fruit](#57-favorite-fruit)
6. [5.8 Hello Admin](#58-hello-admin)
7. [5.9 No Users](#59-no-users)
8. [5.10 Checking Usernames](#510-checking-usernames)
9. [5.11 Ordinal Numbers](#511-ordinal-numbers)

---

### 5.1 Conditional Tests
This exercise demonstrates how to use conditional statements to check the value of variables.

```python
car = 'subaru'
print("Is car == 'subaru'?")
print(car == 'subaru')  # Expected True
print("\nIs car == 'audi'?")
print(car == 'audi')    # Expected False
```

- **Explanation**: Conditional statements are used here to compare the variable `car` with different values. This basic comparison demonstrates `==` (equal to) and `!=` (not equal to).

### 5.2 More Conditional Tests
Shows how to combine conditions using `and` and `or` operators.

```python
age = 18
education = 'Bsc'
print(f"\nIs Hamza's age 27 and education Bsc? {age == 27 and education.lower() == 'bsc'}")
print(f"\nIs Hamza's age 27 or education Bsc? {age == 27 or education.lower() == 'bsc'}\n")
```

- **Explanation**: This exercise introduces the `and` and `or` logical operators. The `and` operator returns `True` only if both conditions are `True`, while the `or` operator returns `True` if at least one condition is `True`.

### 5.3 - 5.5 Alien Colors 1, 2, & 3
Tests conditional logic with `if`, `elif`, and `else` statements to print different messages based on the value of `alien_color`.

```python
alien_color = 'green'
if alien_color == 'green':
    print('Player earned 5 points\n')
elif alien_color == 'yellow':
    print('Player earned 10 points\n')
else:
    print('Player earned 15 points\n')
```

- **Explanation**: Here, the program checks the color of an alien and awards points based on its color. This example demonstrates how to use `if`, `elif`, and `else` to create decision-making branches.

### 5.6 Stages of Life
Categorizes a person’s life stage based on their age.

```python
age = 18
if age < 2:
    print('It is a Baby')
elif age < 4:
    print('It is a toddler')
elif age < 13:
    print('It is a kid')
elif age < 20:
    print('It is a teenager')
elif age < 65:
    print('It is an adult')
else:
    print('It is an elder')
print()
```

- **Explanation**: The program checks multiple age ranges to determine the person’s life stage. This exercise showcases nested conditions with multiple `elif` statements.

### 5.7 Favorite Fruit
Uses a list and `if` statements to check for specific values.

```python
favourite_fruits = ['Apple', 'Banana', 'Pineapple']
if 'Apple' in favourite_fruits:
    print('I really like Apple')
```

- **Explanation**: This example introduces checking if an item is in a list using `in`, and displays a message if a specified fruit is in the list.

### 5.8 Hello Admin
Uses a `for` loop to greet users differently if their username is `'admin'`.

```python
usernames = ['admin', 'Hamza', 'Atiq', 'Saad', 'Umar']
for name in usernames:
    if name == 'admin':
        print(f'Hello {name}! Would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again')
print()
```

- **Explanation**: Here, we loop through a list of usernames and print a special message for the admin user. This introduces control flow in loops with conditional statements.

### 5.9 No Users
Checks if the `usernames` list is empty before proceeding.

```python
usernames = []
if usernames:
    for name in usernames:
        print(f'Hello {name}, welcome back!')
else:
    print('We need to find some users')
print()
```

- **Explanation**: This example introduces checking for an empty list, a common technique to ensure the code only executes when there’s data to work with.

### 5.10 Checking Usernames
Checks for existing usernames before allowing a new one to be created.

```python
current_users = ['admin', 'Hamza', 'Atiq', 'Saad', 'Umar']
new_users = ['admin', 'Hamza', 'Ibtisam', 'Abdullah', 'Abdur Rehman']
current_users_lower = [user.lower() for user in current_users]

for name in new_users:
    if name.lower() in current_users_lower:
        print(f'Username "{name}" is taken, please enter a new username.')
    else:
        print(f'Username "{name}" is available.')
print()
```

- **Explanation**: This program demonstrates case-insensitive comparison of usernames using a lowercase version of `current_users`. It checks for available usernames before adding new users, a useful practice in registration systems.

### 5.11 Ordinal Numbers
Formats numbers to display ordinal indicators (like "1st", "2nd", "3rd").

```python
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
print()
```

- **Explanation**: This example uses conditionals to add the appropriate suffix to each number, making it a great exercise in applying `if-elif-else` statements for data formatting.

---

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.
