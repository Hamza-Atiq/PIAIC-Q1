# 9.1 Restaurant 

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
        print('The restaurant is open. \n')

# Create an instance of Restaurant
restaurant1 = Restaurant('quetta cafe', 'quetta chai')

# Print the attributes individually
print(restaurant1.name)
print(restaurant1.type)

# Call the methods without print() since they handle printing on their own
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

############################################

# 9.2 Three Restaurants

class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """
        Prints the restaurant's name and cuisine type.
        """
        print(f'Restaurant name: {self.name.title()}')
        print(f'Restaurant cuisine type: {self.type.title()} \n')

    def open_restaurant(self):
        """
        Prints a message indicating that the restaurant is open.
        """
        print('The restaurant is open. \n')

# Create an instance of Restaurant
restaurant2 = Restaurant('niko gee', 'fish')
restaurant3 = Restaurant('chezzious' , 'pizza')
restaurant4 = Restaurant('savour food' , 'rice')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

########################################################

# 9.3 Users

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

##################################################

# 9.4 Number Served

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

    def set_number_served(self, numbers_served: int):
        """
        Sets the number of customers served to a specific value.
        """
        self.number_served = numbers_served

    def increment_number_served(self, increment: int):
        """
        Increments the number of customers served by a specified amount.
        """
        self.number_served += increment

# Creating an instance of Restaurant
restaurant5 = Restaurant('tikka boti', 'bbq')

# Printing the initial number of customers served
print(f"Number of customers served: {restaurant5.number_served}")

# Updating the number_served attribute
restaurant5.number_served = 5
print(f"Updated number of customers served: {restaurant5.number_served}\n")

# Using set_number_served method
restaurant5.set_number_served(10)
print(f"Set number of customers served: {restaurant5.number_served}\n")

# Using increment_number_served method
restaurant5.increment_number_served(100)
print(f"Incremented number of customers served: {restaurant5.number_served}\n")

##################################################

# 9.5 Login Attempts 

class User:
    def __init__(self, first_name: str, last_name: str, age: int, 
                 location: str, education: str, profession: str ):
        """
        Initialize user with first name, last name, age, location, education, and profession.
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.education = education.title()
        self.profession = profession.title()
        self.login_attempts = 0

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
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating instances of the User class
user1 = User('abdullah', 'khan', 29, 'rawalpindi', 'msc', 'data scientist')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts , '\n')

############################################

# 9.6 Ice Cream Stand

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

    def set_number_served(self, numbers_served: int):
        """
        Sets the number of customers served to a specific value.
        """
        self.number_served = numbers_served

    def increment_number_served(self, increment: int):
        """
        Increments the number of customers served by a specified amount.
        """
        self.number_served += increment

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type , flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def ice_cream_flavours(self):
        print('These are the ice cream flavours offers by Restaurant : ')
        for flavour in self.flavours:
            print(flavour , '\n')

stand1 = IceCreamStand('tehzeeb' , 'ice creams' , ['mango' , 'banana' , 'stawberry' , 'chocolate'])
stand1.ice_cream_flavours()

##################################################

# 9.7 Admin

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

class Admin(User):

    def __init__(self, first_name, last_name, age, location, education, profession , privileges):
        super().__init__(first_name, last_name, age, location, education, profession)
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges include:")
        for message in self.privileges:
            print(message)

list_of_privileges : list[str] = ['can add post' ,
                                  'can delete post' , 
                                  'can ban user']
admin1 = Admin('hamza', 'atiq', 27, 'rawalpindi', 'bsc', 'generative ai engineer' , list_of_privileges)
admin1.show_privileges()
print()

##########################################

# 9.8 Privileges

class Privileges:

    def __init__(self , privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges include:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):

    def __init__(self, first_name, last_name, age, location, education, profession , privileges = None ):
        super().__init__(first_name, last_name, age, location, education, profession)
        self.privileges = Privileges(privileges if privileges is not None else [])

list_of_privileges : list[str] = ['can add post' ,
                                  'can delete post' , 
                                  'can ban user']

admin3 = Admin('ali' , 'raza' , 27 , 'jhand' , 'bsc' , 'teacher' , list_of_privileges)
admin3.privileges.show_privileges() 
print()

#############################################

# 9.9 Battery Upgrade 

class Car:

    def __init__(self , model , name , year):
        """Initialize attributes to describe a car."""
        self.model = model
        self.name = name
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f'{self.name} {self.model} {self.year}'
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self , mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")   

    def increment_odometer(self , miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:

    def __init__(self , battery_size = 40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size 

    def descibe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
    
class ElecticCar(Car):

    def __init__(self, model, name, year):
        super().__init__(model, name, year)
        self.battery = Battery()
    
# Creating an instance of ElectricCar
car1 = ElecticCar('Honda', 'Civic', 2020)

# Checking the range before battery upgrade
print("Before battery upgrade:")
car1.battery.get_range()

# Upgrading the battery and checking the range again
car1.battery.upgrade_battery()
print("\nAfter battery upgrade:")
car1.battery.get_range()
print()



    

    
