# 5.1 Conditional Tests

car = 'subaru'
print("Is car == 'subaru'?")
print(car == 'subaru')
print("\nIs car == 'audi'?")
print(car == 'audi')
print("\nIs car == 'honda'?")
print(car == 'honda')
print("\nIs car == 'toyota'?")
print(car == 'toyota')
print("\nIs car == 'Subaru'?")
print(car.title() == 'Subaru')

#################################################

# 5.2 More conditional Tests

age = 18
print(f'\nIs Hamza Age is 27 ? {age == 27}')

education = 'Bsc'
print(f"\nIs Hamza's age 27 and education bsc? {age == 27 and education.lower() == 'bsc'}")
print(f"\nIs Hamza's age 27 and education bsc? {age == 27 or education.lower() == 'bsc'} \n")

subjects = ['math' , 'AI' , 'python' , 'Machine learning']
print('deep learning' in subjects , '\n')
print('deep learning' not in subjects , '\n')

# 5.3 & 5.4 & 5.5  Alien Colors 1 , 2 , 3

alien_color : str = 'green' 

if alien_color == 'green':
    print('Player earned 5 points \n')
elif alien_color == 'yellow':
    print('Player earned 10 points \n')
elif alien_color == 'red':
    print('Player earned 15 points')

#########################################

# 5.6 Stages of life

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
    print('It is an elder ')
print()

#################################

# 5.7 Favourite Fruit

favourite_fruits : list[str] = ['Apple' , "Banana" , 'Pineapple']

if 'Apple' in favourite_fruits:
    print('I really like Apple')
elif 'Banana' in favourite_fruits:
    print('I really like Banana')
elif 'Pineaaple' in favourite_fruits:
    print('I really line Pineapple')
else:
    print('This is not my favourite fruit')
print()

###########################################    

# 5.8 Hello Admin

usernames : list[str] = ['admin' , 'Hamza' , 'Atiq' , 'Saad' , 'Umar']

for names in usernames:
    if names == 'admin':
        print(f'Hello {names} ! would you like to see a status report?')
    else:
        print(f'Hello {names}, thank you for logging in again')
print()

########################################

# 5.9 No users

usernames : list[str] = ['admin' , 'Hamza' , 'Atiq' , 'Saad' , 'Umar']
empty_list = []
if empty_list:
    for names in empty_list:
        if names == 'admin':
            print(f'Hello {names} ! would you like to see a status report?')
        else:
            print(f'Hello {names}, thank you for logging in again')
else:
    print('We need to find some users')
    for names in usernames:
        empty_list.append(names)
print(empty_list)
print()

# 5.10 Checking usernames

current_users : list[str] = ['admin' , 'Hamza' , 'Atiq' , 'Saad' , 'Umar']
new_users : list[str] = ['admin' , 'Hamza' , 'Ibtisam' , 'Abdullah' , 'Abdur Rehman']

# Create a lowercase version of current_users to ensure case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for names in new_users:
    if names.lower() in current_users_lower:
        if names.lower() == 'admin':
            print('How may i help you')
        else:
            print('Please enter a new user name ')
    else:
        print('username is available')
print()

#############################################

# 5.11 ordinal numbers

num_list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
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


