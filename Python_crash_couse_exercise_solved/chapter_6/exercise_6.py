# 6.1 Person

person : dict[str , all] = {'first_name' : "Hamza" , 'last_name' : 'Atiq' , 'age' : 27 , 'city' : "Rawalpindi"}
print(f"Person first name is {person['first_name'].upper()} last name is {person['last_name'].upper()}")
print(f"Person age is {person['age']} and he lives in {person['city'].upper()} \n")
 
############################################

# 6.2 Favourite Numbers

peoples_favorite_numbers : dict[str , int] = {
    "Abdullah" : 34,
    "Ali" : 39,
    "Hamza" : 68 ,
    "Abu Bakar" : 17,
    "Kamran" : 58,
}

for name , number in peoples_favorite_numbers.items():
    print(f'{name.upper()} favourite number is {number}')
print()

#########################################

# 6.3 Glossary

glossary : dict[str , str ] = {
    'len' : 'check the length of the list',
    'list' : 'it is represented by []',
    'int' : 'it is used for integers',
    'str' : 'it is used for strings',
    'float' : 'it is used for float values',
}
number : int = 1
for key , value in glossary.items():
    print(f'The {number} programming word is \n{key} : \n    {value} \n')
    number += 1

#################################################

# 6.4 Glossary 2

glossary2 : dict[str , str] = {
    'len' : 'check the length of the list',
    'list' : 'it is represented by []',
    'int' : 'it is used for integers',
    'str' : 'it is used for strings',
    'float' : 'it is used for float values',
    'if-else' : 'used to check the one posiible condition and performs',
    'for' : 'it repeat the task which is in his indentation until condition True',
    'variable' : 'it is used to store the values',
    'input' : 'it is used to get input from the user',
    'print' : 'it is used to display output to the user'
}
number = 1
for key , value in glossary2.items():
    print(f'The {number} programming word is \n{key} : \n    {value} \n')
    number += 1

########################################

# 6.5 Rivers 

rivers : dict[str , str] = {
    'nile' : 'Egypt',
    'indus' : 'Pakistan',
    'amazon' : 'South America'
}

for river , country in sorted(rivers.items()):
    print(f"The {river} runs through {country}")
print()

for river in rivers:
    print(river)
print()

for country in rivers.values():
    print(country)
print()

####################################################

# 6.6 Polling 

favorite_languages : dict[str , str] = {
 'Abdullah': 'python',
 'sarah': 'c',
 'Muarij': 'rust',
 'Hamza': 'python',
}

names_for_poll : list[dict[str , str]] = ['Abdullah' , 'Ali' , 'Kamran' , 'Muarij']

for names in names_for_poll:
    if names in favorite_languages:
        print('Thanks you participate ')
    else:
        print('Please participate in the poll')
print()

##############################################

# 6.7 People

person1 : dict[str , all] = {
    'first_name' : 'Abdullah',
    'last_name' : 'Khan',
    'age' : 29 ,
    'city' : 'Rawalpindi'
}

person2 : dict[str , all] = {
    'first_name' : 'Muarij',
    'last_name' : 'Fasiah',
    'age' : 28 ,
    'city' : 'Lahore'
}

person3 : dict[str , all] = {
    'first_name' : 'Muhammad',
    'last_name' : 'Haseeb',
    'age' : 33 ,
    'city' : 'Karachi'
}

people : list[dict[str , all]] = [person1 , person2  , person3]
number : int = 1
for data in people:
    print(f"Person {number} first name is {data['first_name']} last name is {data['last_name']}")
    print(f"Person {number} age is {data['age']} and he lives in {data['city']} \n")
    number +=1

###############################################

# 6.8 Pets 

# Define each animal as a dictionary with additional name keys
dog: dict[str, str] = {'name': 'Dog', 'kind of animal': 'Domestic', 'owner': 'John'}
cow: dict[str, str] = {'name': 'Cow', 'kind of animal': 'Domestic', 'owner': 'Kamran'}
deer: dict[str, str] = {'name': 'Deer', 'kind of animal': 'Wild', 'owner': 'Young'}
lion: dict[str, str] = {'name': 'Lion', 'kind of animal': 'Wild', 'owner': 'Anderson'}
horse: dict[str, str] = {'name': 'Horse', 'kind of animal': 'Domestic', 'owner': 'Ali'}

# List of pet dictionaries
pets: list[dict[str, str]] = [dog, cow, deer, lion, horse]

# Loop through each pet and print the details
number: int = 1
for pet in pets:
    print(f"The animal {number} name is {pet['name']}! Owner's name is {pet['owner']} and it is a {pet['kind of animal']} animal.")
    number += 1
print()

#################################################

# 6.9 Favorite Places

favorite_places : dict[str , list[str]] = {
    'Abdullah' : ['Gilgit' , 'Makkah' , 'Abbotbad'],
    'Muarij' : ['Lahore' , 'Makkah'],
    'Hamza' : ['Makkah'],
} 

for name , places in favorite_places.items():
    if len(places) > 1:
        print(f'{name} favourite places are {places}')
    else:
        print(f'{name} favourite place is {places}')
print()

#####################################

# 6.10 Favorite Numbers

peoples_favorite_numbers : dict[str , list[int]] = {
    "Abdullah" : [34 , 48 , 52] ,
    "Ali" : [39 , 19] ,
    "Hamza" : [68] ,
    "Abu Bakar" : [17 , 28 , 54] , 
    "Kamran" : [58 , 87],
}

for name , number in peoples_favorite_numbers.items():
    if len(number) > 1:
        print(f'{name} favourite numbers are {number}')
    else:
        print(f'{name} favourite number is {number}')
print()

##################################################

# 6.11 Cities 

cities : dict[str , dict[str , str]] = {
    'Rawalpindi' : {'country' : 'Pakistan' , 'population' : '14 millon' , 'fact' : 'nearer to capital Islamabad'},
    'Lahore' : {'country' : 'Pakistan' , 'population' : '24 millon' , 'fact' : 'nearer to india boarder'},
    'Karachi' : {'country' : 'Pakistan' , 'population' : '44 millon' , 'fact' : 'nearer to Arabian sea'},
}

for city , information in cities.items():
    print(f'{city} is a city of {information['country']} , its population is {information['population']} and it is {information['fact']}')
print()



