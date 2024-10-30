
# Chapter 6: Python Dictionary Exercises

This repository contains a series of Python exercises from Chapter 6, showcasing practical usage of dictionaries, list operations, and loops. These exercises are organized to build familiarity with dictionary structures and their various applications. Below, each exercise is explained in detail with the associated code and comments.

---

## Exercise 6.1: Person

This exercise creates a dictionary containing personal information, then prints the formatted details using dictionary keys.

```python
# 6.1 Person
person : dict[str , all] = {'first_name' : "Hamza" , 'last_name' : 'Atiq' , 'age' : 27 , 'city' : "Rawalpindi"}
print(f"Person first name is {person['first_name'].upper()} last name is {person['last_name'].upper()}")
print(f"Person age is {person['age']} and he lives in {person['city'].upper()} \n")
```

**Explanation**:
This code defines a dictionary, `person`, containing basic details and prints each in a formatted string.

---

## Exercise 6.2: Favorite Numbers

A dictionary stores names as keys and favorite numbers as values. The code then iterates through and prints each person's favorite number.

```python
# 6.2 Favorite Numbers
peoples_favorite_numbers : dict[str , int] = {
    "Abdullah" : 34,
    "Ali" : 39,
    "Hamza" : 68 ,
    "Abu Bakar" : 17,
    "Kamran" : 58,
}

for name , number in peoples_favorite_numbers.items():
    print(f'{name.upper()} favorite number is {number}')
print()
```

**Explanation**:
Using a loop, we display each person's name (converted to uppercase) along with their favorite number.

---

## Exercise 6.3: Glossary

This exercise defines a dictionary where programming terms are keys and their meanings are values, printed one by one.

```python
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
```

**Explanation**:
The glossary terms are looped over with a counter variable, `number`, to list terms and definitions in a structured format.

---

## Exercise 6.4: Glossary 2

An extension of the previous exercise, this glossary contains more terms and definitions.

```python
# 6.4 Glossary 2
glossary2 : dict[str , str] = {
    'len' : 'check the length of the list',
    'list' : 'it is represented by []',
    'int' : 'it is used for integers',
    'str' : 'it is used for strings',
    'float' : 'it is used for float values',
    'if-else' : 'used to check the one possible condition and performs',
    'for' : 'it repeats the task which is in his indentation until condition True',
    'variable' : 'it is used to store the values',
    'input' : 'it is used to get input from the user',
    'print' : 'it is used to display output to the user'
}
number = 1
for key , value in glossary2.items():
    print(f'The {number} programming word is \n{key} : \n    {value} \n')
    number += 1
```

**Explanation**:
This code is similar to the previous, listing more definitions, with some added commentary to further clarify each term's role.

---

## Exercise 6.5: Rivers

This program prints rivers and the countries they run through. Additional loops list the rivers and countries separately.

```python
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
```

**Explanation**:
This example displays each river and the country it runs through, followed by individual lists of rivers and countries.

---

## Exercise 6.6: Polling

This code asks people to take a poll, checking if their name is in a predefined dictionary of `favorite_languages`.

```python
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
        print('Thanks for participating ')
    else:
        print('Please participate in the poll')
print()
```

**Explanation**:
The program checks if people in `names_for_poll` are listed in `favorite_languages`. If they are, they receive a thank-you message; if not, they are invited to participate.

---

### Exercise 6.7: People

This exercise defines multiple dictionaries representing individuals and stores them in a list, then loops through each entry to print the details.

```python
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
```

**Explanation**:  
Each dictionary represents a person with their first name, last name, age, and city. The list `people` stores these dictionaries, which are then accessed using a loop to print each person's information in a structured way.

---

### Exercise 6.8: Pets

This exercise lists different animals as dictionaries with details, and stores them in a list. Each pet's details are printed in a loop.

```python
# 6.8 Pets
dog: dict[str, str] = {'name': 'Dog', 'kind of animal': 'Domestic', 'owner': 'John'}
cow: dict[str, str] = {'name': 'Cow', 'kind of animal': 'Domestic', 'owner': 'Kamran'}
deer: dict[str, str] = {'name': 'Deer', 'kind of animal': 'Wild', 'owner': 'Young'}
lion: dict[str, str] = {'name': 'Lion', 'kind of animal': 'Wild', 'owner': 'Anderson'}
horse: dict[str, str] = {'name': 'Horse', 'kind of animal': 'Domestic', 'owner': 'Ali'}
pets: list[dict[str, str]] = [dog, cow, deer, lion, horse]

number: int = 1
for pet in pets:
    print(f"The animal {number} name is {pet['name']}! Owner's name is {pet['owner']} and it is a {pet['kind of animal']} animal.")
    number += 1
print()
```

**Explanation**:  
This code defines multiple pet dictionaries, each containing the pet's name, kind, and owner. A loop iterates through the list, displaying each pet's details with a counter for clarity.

---

### Exercise 6.9: Favorite Places

This program creates a dictionary where each person has a list of favorite places. The code iterates over the dictionary to print each person's preferences.

```python
# 6.9 Favorite Places
favorite_places : dict[str , list[str]] = {
    'Abdullah' : ['Gilgit' , 'Makkah' , 'Abbotbad'],
    'Muarij' : ['Lahore' , 'Makkah'],
    'Hamza' : ['Makkah'],
} 

for name , places in favorite_places.items():
    if len(places) > 1:
        print(f'{name} favorite places are {places}')
    else:
        print(f'{name} favorite place is {places}')
print()
```

**Explanation**:  
This code stores each person's favorite places in a dictionary as a list. It checks if there are multiple places to tailor the output accordingly, ensuring each person’s places are displayed properly.

---

### Exercise 6.10: Favorite Numbers

In this exercise, multiple favorite numbers are associated with each person. The code iterates over the dictionary to display these numbers.

```python
# 6.10 Favorite Numbers
peoples_favorite_numbers : dict[str , list[int]] = {
    "Abdullah" : [34 , 48 , 52],
    "Ali" : [39 , 19],
    "Hamza" : [68],
    "Abu Bakar" : [17 , 28 , 54], 
    "Kamran" : [58 , 87],
}

for name , number in peoples_favorite_numbers.items():
    if len(number) > 1:
        print(f'{name} favorite numbers are {number}')
    else:
        print(f'{name} favorite number is {number}')
print()
```

**Explanation**:  
A dictionary stores each person's favorite numbers as a list, which are displayed based on whether each person has one or multiple favorite numbers.

---

### Exercise 6.11: Cities

This dictionary contains nested dictionaries, with each city storing details about the country, population, and a fun fact. The code iterates over the nested dictionaries to print each city’s information.

```python
# 6.11 Cities
cities : dict[str , dict[str , str]] = {
    'Rawalpindi' : {'country' : 'Pakistan' , 'population' : '14 million' , 'fact' : 'near the capital Islamabad'},
    'Lahore' : {'country' : 'Pakistan' , 'population' : '24 million' , 'fact' : 'near the India border'},
    'Karachi' : {'country' : 'Pakistan' , 'population' : '44 million' , 'fact' : 'near the Arabian Sea'},
}

for city , information in cities.items():
    print(f"{city} is a city of {information['country']} with a population of {information['population']} and is {information['fact']}.")
print()
```

**Explanation**:  
Each city is represented as a dictionary containing details like country, population, and an interesting fact. A loop accesses each city’s information and presents it in a readable format.

---

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.
