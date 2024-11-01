# 7.1 Rental Car

try:
  car: str = input('What kind of rental car you would like? ')
  if not car.isdigit():  # Check if the input contains only digits
    print(f"Let me see if I can find you a {car}")
  else:
    print("Invalid input! Please enter a valid car type (letters only).")
except ValueError:
  print('Invalid input') 
  
########################################

# 7.2 Restaurant Seating

num_of_people : str = input('How many people are in their dinner group : ')
num_of_people : int = int(num_of_people)
if num_of_people > 8:
    print('You Have to wait for a Table')
else:
    print('Their table is Ready')

###########################################

# 7.3 Multiples of ten

num : int = int(input('Enter any Number : '))
if num % 10 == 0:
   print(f'{num} is a multiple of 10')
else:
   print(f'{num} is not a multiple of 10')

############################################

# 7.4 pizza Toppings

prompt : str = "Enter a series of pizza toppings that you want! "
prompt += "Enter 'quit' to stop: "

flag : bool = True
while flag:
    topping : str = input(prompt)
    if topping.lower() == 'quit':
        flag : bool = False
    else:
        print(f"I'll add {topping} to your pizza.")

############################################

# 7.5 Movie Tickets

prompt: str = "Do you want to buy a ticket? "
prompt += "Enter 'yes' for yes and 'no' for no: "

age_prompt : str = "Enter your age: "

flag : bool = True
while flag:
    requirement = input(prompt)
    if requirement.lower() == 'yes':
        age : str = input(age_prompt)
        if age.isdigit():
            age : int = int(age)
            if age < 3:
                print("Your ticket is free.")
            elif 3 <= age <= 12:
                print("Your ticket is $10.")
            else:
                print("Your ticket is $15.")
        else:
            print("Invalid input. Please enter a valid age.")
    elif requirement.lower() == 'no':
        flag : bool = False
        print("Thank you! Enjoy your day.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


###########################################

# 7.6 Three Exists

prompt : str = "Enter a series of pizza toppings that you want! "
prompt += "Enter 'quit' to stop: "

checking : int = 0

# Use a while loop with a condition that will keep it running
while True:  # Loop will run indefinitely until 'quit' is entered
    topping : str = input(prompt)
    
    if topping.lower() == 'quit':  # Check for quit
        break  # Exit the loop if 'quit' is entered
    
    print(f"I'll add {topping} to your pizza.")  # Acknowledgment of the topping
    checking += 1  # Increment the count of toppings

print(f"The program ran {checking} times.")

################################################

# 7.8 Deli

sandwich_orders : list[str] = ['Tuna sandwich', 'Avocado sandwich', 'Egg sandwich', 'Sabih sandwich', 'Pastrami sandwich']
finished_sandwiches : list[str] = []

while sandwich_orders:
    sandwich : str = sandwich_orders.pop()
    print(f"I made your {sandwich}.")  # Minor improvement for readability
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#####################################################

# 7.9 No Pastrami

sandwich_orders : list[str] = [
    'Tuna sandwich', 'Pastrami sandwich', 'Avocado sandwich', 
    'Egg sandwich', 'Pastrami sandwich', 'Sabih sandwich', 'Pastrami sandwich'
]
finished_sandwiches : list[str] = []

# Notify the user that pastrami is out of stock
print("The deli has run out of pastrami.")

# Remove all 'Pastrami sandwich' occurrences from sandwich_orders
while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

# Process remaining sandwiches in sandwich_orders
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

# Final message showing all finished sandwiches
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

######################################################

# 7.10 Dream Vacation

responses = {}  # Store user responses in a dictionary

while True:
    name : str = input("What is your name? (or type 'quit' to end): ")
    if name.lower() == "quit":
      break

    response : str = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response

print("\nPoll Results:")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response}.")

