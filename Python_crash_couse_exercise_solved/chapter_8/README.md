
# Chapter 8: Functions

This chapter covers defining and using functions in Python, including parameters, return values, arbitrary arguments, and keyword arguments. Each exercise introduces new aspects of function usage and aims to help us build reusable, modular code.

---

## Table of Contents

1. [Display Message](#1-display-message)
2. [Favorite Book](#2-favorite-book)
3. [T-Shirt](#3-t-shirt)
4. [Large Shirts](#4-large-shirts)
5. [Cities](#5-cities)
6. [City Names](#6-city-names)
7. [Album](#7-album)
8. [User Albums](#8-user-albums)
9. [Messages](#9-messages)
10. [Sending Messages](#10-sending-messages)
11. [Archived Messages](#11-archived-messages)
12. [Sandwiches](#12-sandwiches)
13. [User Profile](#13-user-profile)
14. [Cars](#14-cars)

---

### 1. Display Message

**Description**: This function prints a message about what we're learning in this chapter.

```python
def display_message():
    """
    Program about what we learn in this chapter.
    """
    print('This chapter is about user-defined functions.')

display_message()
```

This function has no parameters and simply prints a message when called.

---

### 2. Favorite Book

**Description**: This function takes a book title as an argument and prints it in a formatted string.

```python
def favorite_book(title: str):
    print(f'My favorite book is {title.title()}.')

favorite_book('quran majeed')
```

The function demonstrates passing an argument to a function and using string formatting.

---

### 3. T-Shirt

**Description**: This function accepts a size and text for a T-shirt and prints a summary of the order.

```python
def make_shirt(size: str, text: str):
    print(f'Your shirt size is: {size} and you want to write: {text}')

make_shirt('medium', 'I love you')
make_shirt(text='Pakistan Zindabad', size='small')
```

This example shows both positional and keyword arguments in function calls.

---

### 4. Large Shirts

**Description**: This function demonstrates default values for parameters.

```python
def make_shirt(size: str = 'large', text: str = 'I love Python'):
    print(f'Your shirt size is: {size} and you want to write: {text}')

make_shirt()
make_shirt(size='medium')
make_shirt(text='I love Imran Khan')
```

If no arguments are passed, it defaults to a "large" size and the text "I love Python".

---

### 5. Cities

**Description**: This function describes a city and its country, with a default country value of "Pakistan".

```python
def describe_city(city: str, country: str = 'Pakistan'):
    print(f'{city.title()} is in {country.title()}.')

describe_city('rawalpindi')
describe_city('lahore')
describe_city('new york', country='America')
```

Demonstrates default parameter values and overriding the default with an argument.

---

### 6. City Names

**Description**: This function returns a formatted string with city and country names.

```python
def city_country(city: str, country: str) -> str:
    sentence = f"{city}, {country}"
    return sentence.title()

one = city_country('rawalpindi', 'pakistan')
two = city_country('makkah', 'saudi arabia')
three = city_country('lahore', 'pakistan')
print(one, '\n', two, '\n', three)
```

Illustrates the use of `return` to pass back a formatted string.

---

### 7. Album

**Description**: This function returns a dictionary containing information about an album. The number of songs is optional.

```python
def make_album(artist_name: str, album_title: str, number_of_songs: int = None) -> dict:
    album = {'Artist_Name': artist_name, 'Album_Title': album_title}
    if number_of_songs:
        album['num_of_songs'] = number_of_songs
    return album

album1 = make_album('Ali', 'Tara Zameen Par')
album2 = make_album('Farhan', 'Ham Sab 1 Hain')
album3 = make_album('Farooq', 'Laggan')
album4 = make_album('Kiran', 'Khobsorti', 5)

print(album1, '\n', album2, '\n', album3, '\n', album4)
```

Shows the use of optional parameters to create a dictionary with or without an additional attribute.

---

### 8. User Albums

**Description**: This program repeatedly asks the user for album details, allowing the user to quit at any time.

```python
while True:
    artist_name = input('Enter the artist name (or "q" to quit): ')
    if artist_name.lower() == 'q':
        break
    
    album_title = input('Enter the album title (or "q" to quit): ')
    if album_title.lower() == 'q':
        break
    
    num_songs = input('Enter the number of songs (or "q" to quit): ')
    if num_songs.lower() == 'q':
        break
    
    if num_songs.isdigit():
        num_songs = int(num_songs)
    else:
        num_songs = None
    
    album = make_album(artist_name, album_title, num_songs)
    print(f"\nAlbum details: {album}\n")
```

Uses a loop and `make_album` function to continuously collect album data.

---

### 9. Messages

**Description**: This function accepts a list of messages and prints each one.

```python
def show_messages(messages: list[str]):
    for message in messages:
        print(message)

messages = [
    'My name is Hamza Atiq',
    'I am a student of PIAIC',
    'My aim is to become an AI developer',
    'I will run a software house in the next 5 years, Insha Allah'
]

show_messages(messages)
```

---

### 10. Sending Messages

**Description**: This function moves each message from one list to another after printing it.

```python
def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.append(message)

sent_messages = []
messages = [
    'My name is Hamza Atiq',
    'I am a student of PIAIC',
    'My aim is to become an AI developer',
    'I will run a software house in the next 5 years, Insha Allah'
]

send_messages(messages, sent_messages)
print("\nOriginal messages list (should be empty):", messages)
print("Sent messages list (should contain all messages):", sent_messages)
```

---

### 11. Archived Messages

**Description**: This version of `send_messages` creates a copy of the list to keep the original intact.

```python
send_messages(messages[:], sent_messages)
print("\nOriginal messages list (not empty):", messages)
print("Sent messages list (should contain all messages):", sent_messages)
```

---

### 12. Sandwiches

**Description**: This function accepts any number of sandwich ingredients and summarizes the sandwich order.

```python
def sandwiches(*ingredients: str) -> None:
    print("The following items have been added to your sandwich:")
    for item in ingredients:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

sandwiches('Tuna', 'Avocado', 'Egg', 'Pastrami')
sandwiches('Egg', 'Mayonnaise', 'Ketchup')
sandwiches('Sauce', 'Olives', 'Butter')
```

---

### 13. User Profile

**Description**: This function builds a user profile with arbitrary keyword arguments.

```python
def build_profile(first: str, last: str, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('hamza', 'atiq', education='Bsc', location='Rawalpindi', hobby='coding')
print(user_profile)
```

---

### 14. Cars

**Description**: This function builds a dictionary containing car details using keyword arguments for flexibility.

```python
def make_car(manufacturer: str, model_name: str, **car_data) -> dict:
    car_info = {
        'manufacturer': manufacturer.title(),
        'model_name': model_name.title()
    }
    car_info.update(car_data)
    return car_info

car = make_car('suzuki', 'old version', owner_name='Uzair', year_of_purchasing='2019', color='grey', tow_package=True)
print(car)
```

---

## Conclusion

These exercises provide hands-on practice with defining functions, setting default values, working with arbitrary and keyword arguments, and returning values in Python. Functions are essential for creating modular and reusable code.

---

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.