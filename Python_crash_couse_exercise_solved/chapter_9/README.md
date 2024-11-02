Here's the formatted Markdown file for Chapter 9 exercises. This includes explanations, improved formatting, and corrections where needed.

---

# Chapter 9: Classes

In this chapter, we explore Python classes and objects. These exercises involve defining classes, initializing attributes, and creating methods to interact with instances.

---

## Table of Contents

1. [Restaurant](#1-restaurant)
2. [Three Restaurants](#2-three-restaurants)
3. [Users](#3-users)
4. [Number Served](#1-number-served)
5. [Login Attempts](#2-login-attempts)


---

### 1. Restaurant

**Description**: This exercise defines a `Restaurant` class with two attributes (`restaurant_name` and `cuisine_type`) and two methods (`describe_restaurant` and `open_restaurant`).

```python
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """
        Prints the restaurant's name and cuisine type.
        """
        print(f'Restaurant name: {self.name.title()}')
        print(f'Restaurant cuisine type: {self.type.title()}')

    def open_restaurant(self):
        """
        Prints a message indicating that the restaurant is open.
        """
        print('The restaurant is open.\n')

# Create an instance of Restaurant
restaurant1 = Restaurant('quetta cafe', 'quetta chai')

# Print the attributes individually
print(restaurant1.name)
print(restaurant1.type)

# Call the methods without print() since they handle printing on their own
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
```

In this example, we create an instance of `Restaurant` and print its attributes directly. The methods are then called to display additional information.

---

### 2. Three Restaurants

**Description**: This exercise creates three instances of the `Restaurant` class and calls the `describe_restaurant` method for each.

```python
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """
        Prints the restaurant's name and cuisine type.
        """
        print(f'Restaurant name: {self.name.title()}')
        print(f'Restaurant cuisine type: {self.type.title()}\n')

    def open_restaurant(self):
        """
        Prints a message indicating that the restaurant is open.
        """
        print('The restaurant is open.\n')

# Create instances of Restaurant
restaurant2 = Restaurant('niko gee', 'fish')
restaurant3 = Restaurant('chezzious', 'pizza')
restaurant4 = Restaurant('savour food', 'rice')

# Calling describe_restaurant method for each instance
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()
```

This exercise demonstrates creating multiple instances of a class and calling a method on each instance to display unique information.

---

### 3. Users

**Description**: This exercise defines a `User` class with attributes for first name, last name, age, location, education, and profession. The class has two methods: `describe_user` and `greet_user`.

```python
class User:
    def __init__(self, first_name: str, last_name: str, age: int, location: str, education: str, profession: str):
        """
        Initialize user with first name, last name, age, location, education, and profession.
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.education = education.title()
        self.profession = profession.title()

    def describe_user(self):
        """
        Print a summary of the user's information.
        """
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"They live in {self.location}. They completed their {self.education}.")
        print(f"They work as a {self.profession}.\n")

    def greet_user(self):
        """
        Print a personalized greeting for the user.
        """
        print(f"Welcome {self.first_name} {self.last_name}!\n")

# Creating instances of the User class
user1 = User('abdullah', 'khan', 29, 'rawalpindi', 'msc', 'data scientist')
user2 = User('muarij', 'fasiah', 30, 'lahore', 'bsc', 'front end developer')
user3 = User('hamza', 'atiq', 27, 'rawalpindi', 'bsc', 'generative ai engineer')

# Calling methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
```

This code demonstrates how to initialize instances with personal data and create methods that interact with the attributes.

---

### 4. Number Served

**Description**: This exercise enhances the `Restaurant` class by adding a `number_served` attribute to keep track of the number of customers served. It also includes methods to set and increment this value.

```python
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """
        Initialize the restaurant with a name, cuisine type, and default number of customers served.
        """
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0  # Default value for the number of customers served

    def describe_restaurant(self):
        """
        Prints the restaurant's name and cuisine type.
        """
        print(f'Restaurant name: {self.name.title()}')
        print(f'Restaurant cuisine type: {self.type.title()}')

    def open_restaurant(self):
        """
        Prints a message indicating that the restaurant is open.
        """
        print('The restaurant is open.\n')

    def set_number_served(self, number_served: int):
        """
        Sets the number of customers served to a specific value.
        """
        self.number_served = number_served

    def increment_number_served(self, increment: int):
        """
        Increments the number of customers served by a specified amount.
        """
        self.number_served += increment

# Creating an instance of Restaurant
restaurant5 = Restaurant('tikka boti', 'bbq')

# Printing the initial number of customers served
print(f"Number of customers served: {restaurant5.number_served}")

# Updating the number_served attribute directly
restaurant5.number_served = 5
print(f"Updated number of customers served: {restaurant5.number_served}\n")

# Using set_number_served method to set a specific value
restaurant5.set_number_served(10)
print(f"Set number of customers served: {restaurant5.number_served}\n")

# Using increment_number_served method to increase by a specified amount
restaurant5.increment_number_served(100)
print(f"Incremented number of customers served: {restaurant5.number_served}\n")
```

In this example, we create an instance of `Restaurant` and demonstrate three ways to modify the `number_served` attribute: directly, by setting a specific number, and by incrementing.

---

### 5. Login Attempts

**Description**: This exercise adds a `login_attempts` attribute to the `User` class and methods to increment, reset, and check the login attempts.

```python
class User:
    def __init__(self, first_name: str, last_name: str, age: int, location: str, education: str, profession: str):
        """
        Initialize user with first name, last name, age, location, education, and profession.
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.education = education.title()
        self.profession = profession.title()
        self.login_attempts = 0  # Tracks the number of login attempts

    def describe_user(self):
        """
        Print a summary of the user's information.
        """
        print(f"{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"They live in {self.location}. They completed their {self.education}.")
        print(f"They work as a {self.profession}.\n")

    def greet_user(self):
        """
        Print a personalized greeting for the user.
        """
        print(f"Welcome {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        """
        Increment the number of login attempts by 1.
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """
        Reset the number of login attempts to 0.
        """
        self.login_attempts = 0

# Creating an instance of User and simulating login attempts
user1 = User('abdullah', 'khan', 29, 'rawalpindi', 'msc', 'data scientist')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the current login attempts count
print(f"Login attempts: {user1.login_attempts}")

# Reset login attempts and print again to verify reset
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}\n")
```

In this example, the `increment_login_attempts` method is used to simulate multiple login attempts, while the `reset_login_attempts` method clears the login count.

---

