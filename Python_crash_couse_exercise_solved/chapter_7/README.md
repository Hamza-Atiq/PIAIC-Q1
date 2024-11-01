
# Chapter 7: User Input and While Loops

This chapter covers various programs that take user input, use conditional statements, and demonstrate the usage of `while` loops for repeated actions. Below is a summary of each exercise, code, and explanation.

---

## Table of Contents

1. [Rental Car](#1-rental-car)
2. [Restaurant Seating](#2-restaurant-seating)
3. [Multiples of Ten](#3-multiples-of-ten)
4. [Pizza Toppings](#4-pizza-toppings)
5. [Movie Tickets](#5-movie-tickets)
6. [Three Exits](#6-three-exits)
7. [Deli](#7-deli)
8. [No Pastrami](#8-no-pastrami)
9. [Dream Vacation](#9-dream-vacation)

---

### 1. Rental Car

**Description**: This program asks the user what type of rental car they would like, verifying their input.

```python
try:
    car: str = input('What kind of rental car would you like? ')
    if not car.isdigit():
        print(f"Let me see if I can find you a {car}")
    else:
        print("Invalid input! Please enter a valid car type (letters only).")
except ValueError:
    print('Invalid input')
```

This code ensures the user provides a valid car type and returns a friendly message.

---

### 2. Restaurant Seating

**Description**: This program checks if there is a table available based on the size of the dinner group.

```python
num_of_people: str = input('How many people are in their dinner group: ')
num_of_people: int = int(num_of_people)
if num_of_people > 8:
    print('You have to wait for a table.')
else:
    print('Your table is ready.')
```

It asks the user for the number of people and informs if they need to wait based on the group size.

---

### 3. Multiples of Ten

**Description**: This program checks if a given number is a multiple of ten.

```python
num: int = int(input('Enter any number: '))
if num % 10 == 0:
    print(f'{num} is a multiple of 10')
else:
    print(f'{num} is not a multiple of 10')
```

The program uses modulo operation to determine if the input number is divisible by ten.

---

### 4. Pizza Toppings

**Description**: This program repeatedly asks for pizza toppings until the user decides to stop.

```python
prompt: str = "Enter a series of pizza toppings that you want! Enter 'quit' to stop: "
flag: bool = True
while flag:
    topping: str = input(prompt)
    if topping.lower() == 'quit':
        flag = False
    else:
        print(f"I'll add {topping} to your pizza.")
```

The program continues to accept toppings and acknowledges each entry until 'quit' is entered.

---

### 5. Movie Tickets

**Description**: This program determines the cost of a movie ticket based on the user's age.

```python
prompt: str = "Do you want to buy a ticket? Enter 'yes' for yes and 'no' for no: "
age_prompt: str = "Enter your age: "

flag: bool = True
while flag:
    requirement = input(prompt)
    if requirement.lower() == 'yes':
        age: str = input(age_prompt)
        if age.isdigit():
            age: int = int(age)
            if age < 3:
                print("Your ticket is free.")
            elif 3 <= age <= 12:
                print("Your ticket is $10.")
            else:
                print("Your ticket is $15.")
        else:
            print("Invalid input. Please enter a valid age.")
    elif requirement.lower() == 'no':
        flag = False
        print("Thank you! Enjoy your day.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
```

This program handles user responses and ticket pricing based on age.

---

### 6. Three Exits

**Description**: This program simulates a pizza ordering process where the loop exits when 'quit' is entered.

```python
prompt: str = "Enter a series of pizza toppings that you want! Enter 'quit' to stop: "
checking: int = 0

while True:
    topping: str = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")
    checking += 1

print(f"The program ran {checking} times.")
```

The loop runs indefinitely until 'quit' is entered, counting the number of times toppings are added.

---

### 7. Deli

**Description**: This program processes sandwich orders from a list and moves them to a finished list.

```python
sandwich_orders: list[str] = ['Tuna sandwich', 'Avocado sandwich', 'Egg sandwich', 'Sabih sandwich', 'Pastrami sandwich']
finished_sandwiches: list[str] = []

while sandwich_orders:
    sandwich: str = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
```

This program iterates through orders, making each sandwich and displaying the finished sandwiches list.

---

### 8. No Pastrami

**Description**: This program removes 'Pastrami sandwich' from the orders due to stock shortage and then processes the remaining orders.

```python
sandwich_orders: list[str] = [
    'Tuna sandwich', 'Pastrami sandwich', 'Avocado sandwich', 
    'Egg sandwich', 'Pastrami sandwich', 'Sabih sandwich', 'Pastrami sandwich'
]
finished_sandwiches: list[str] = []

print("The deli has run out of pastrami.")

while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
```

The program removes all 'Pastrami sandwich' orders before processing the remaining ones.

---

### 9. Dream Vacation

**Description**: This program conducts a poll asking users about their dream vacation destinations.

```python
responses = {}

while True:
    name: str = input("What is your name? (or type 'quit' to end): ")
    if name.lower() == "quit":
        break

    response: str = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response

print("\nPoll Results:")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response}.")
```

The program collects responses and displays a summary of the dream destinations chosen by users.

---

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.