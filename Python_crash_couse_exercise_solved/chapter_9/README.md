
# Chapter 9: Classes

In this chapter, we explore Python classes and objects. These exercises involve defining classes, initializing attributes, and creating methods to interact with instances.

---

## Table of Contents

1. [Restaurant](#1-restaurant)
2. [Three Restaurants](#2-three-restaurants)
3. [Users](#3-users)
4. [Number Served](#1-number-served)
5. [Login Attempts](#2-login-attempts)
6. [Ice Cream Stand](#1-ice-cream-stand)
7. [Admin](#2-admin)
8. [Privileges](#3-privileges)
9. [Battery Upgrade](#4-battery-upgrade)


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

### 6. Ice Cream Stand

**Description**: This exercise demonstrates inheritance by creating a subclass, `IceCreamStand`, derived from the `Restaurant` class. We add a `flavours` attribute and a method to display available flavors.

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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def ice_cream_flavours(self):
        """
        Prints the list of available ice cream flavors.
        """
        print("Ice cream flavors offered by the restaurant:")
        for flavour in self.flavours:
            print(f"- {flavour}")

# Creating an instance of IceCreamStand
stand1 = IceCreamStand('Tehzeeb', 'Ice Creams', ['Mango', 'Banana', 'Strawberry', 'Chocolate'])
stand1.ice_cream_flavours()
```

---

### 7. Admin

**Description**: This exercise uses inheritance to create an `Admin` class based on the `User` class, adding a `privileges` attribute and a method to display admin-specific privileges.

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

class Admin(User):
    def __init__(self, first_name, last_name, age, location, education, profession, privileges):
        super().__init__(first_name, last_name, age, location, education, profession)
        self.privileges = privileges

    def show_privileges(self):
        """
        Prints the list of admin privileges.
        """
        print("Admin privileges include:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Example usage
list_of_privileges = ['can add post', 'can delete post', 'can ban user']
admin1 = Admin('Hamza', 'Atiq', 27, 'Rawalpindi', 'BSc', 'Generative AI Engineer', list_of_privileges)
admin1.show_privileges()
```

---

### 8. Privileges

**Description**: This exercise refines the `Admin` class by creating a `Privileges` class, encapsulating privileges in a separate class.

```python
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """
        Prints the list of privileges.
        """
        print("Admin privileges include:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, education, profession, privileges=None):
        super().__init__(first_name, last_name, age, location, education, profession)
        self.privileges = Privileges(privileges if privileges is not None else [])

# Example usage
list_of_privileges = ['can add post', 'can delete post', 'can ban user']
admin2 = Admin('Ali', 'Raza', 27, 'Jhand', 'BSc', 'Teacher', list_of_privileges)
admin2.privileges.show_privileges()
```

---

### 9. Battery Upgrade

**Description**: This exercise demonstrates a nested class by creating a `Battery` class that manages battery-specific details within an `ElectricCar` class. A method to upgrade the battery capacity is also provided.

```python
class Car:
    def __init__(self, model, name, year):
        """
        Initialize attributes to describe a car.
        """
        self.model = model
        self.name = name
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name.
        """
        return f"{self.name} {self.model} {self.year}".title()

    def read_odometer(self):
        """
        Print a statement showing the car's mileage.
        """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

class Battery:
    def __init__(self, battery_size=40):
        """
        Initialize the battery's attributes.
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """
        Print a statement about the range this battery provides.
        """
        range = 150 if self.battery_size == 40 else 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """
        Upgrade the battery capacity if it is not already at the maximum.
        """
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, model, name, year):
        super().__init__(model, name, year)
        self.battery = Battery()

# Example usage
car1 = ElectricCar('Honda', 'Civic', 2020)

# Checking the range before battery upgrade
print("Before battery upgrade:")
car1.battery.get_range()

# Upgrading the battery and checking the range again
car1.battery.upgrade_battery()
print("\nAfter battery upgrade:")
car1.battery.get_range()
```

---
