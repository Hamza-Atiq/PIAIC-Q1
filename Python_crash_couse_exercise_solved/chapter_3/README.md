
# Python Exercises - Book Chapter 3

Welcome to my GitHub repository for Python exercises. Here, I share my progress through the exercises in Chapter 3 of a Python book, focusing on list manipulation, basic list functions, and basic control over list elements.

## Table of Contents
1. [3.1 Names](#31-names)
2. [3.2 Greetings](#32-greetings)
3. [3.3 Your Own List](#33-your-own-list)
4. [3.4 Guest List](#34-guest-list)
5. [3.5 Changing Guest List](#35-changing-guest-list)
6. [3.6 More Guests](#36-more-guests)
7. [3.7 Shrinking Guest List](#37-shrinking-guest-list)
8. [3.8 Seeing the World](#38-seeing-the-world)
9. [3.9 Length of List](#39-length-of-list)
10. [3.10 Every Function](#310-every-function)

---

### 3.1 Names
Prints the names of friends from a list.

```python
list_of_friends_name = ['Abdullah', 'Muraj', 'Arslan']
print(list_of_friends_name)
print(list_of_friends_name[0])
print(list_of_friends_name[1])
print(list_of_friends_name[2], '\n')
```

### 3.2 Greetings
Displays personalized greetings for each friend in the list.

```python
print(f'Assalamo Alaikum! How are you {list_of_friends_name[0]}! Welcome to my house.')
print(f'Assalamo Alaikum! How are you {list_of_friends_name[1]}! Welcome to my house.')
print(f'Assalamo Alaikum! How are you {list_of_friends_name[2]}! Welcome to my house.\n')
```

### 3.3 Your Own List
Creates a list of items the user likes and prints statements about each item.

```python
items_list = ['Motorcycle', 'Laptop', 'Car', 'Mobile']
print(f'I love Honda {items_list[0]}')
print(f'I mostly use {items_list[1]}')
print(f'My aim is to buy a Vezel {items_list[2]}')
print(f'My {items_list[3]} is an Infinix Smart 5\n')
```

### 3.4 Guest List
Displays invitation messages for a list of family members.

```python
list_of_family_members = ['Mother', 'Father', 'Sister', 'Brother']
for member in list_of_family_members:
    print(f'Respected {member}, I am very happy if you join the dinner on Sunday.')
print()
```

### 3.5 Changing Guest List
Replaces one family member with another and displays updated invitation messages.

```python
print(f'My {list_of_family_members[3]} is busy and cannot attend the dinner.')
list_of_family_members[3] = 'Uncle'
for member in list_of_family_members:
    print(f'Respected {member}, I am very happy if you join the dinner on Sunday.')
print() 
```

### 3.6 More Guests
Adds more guests to the list using `insert` and `append` methods, then displays new invitation messages.

```python
print('I want to invite more people to the dinner.')
list_of_family_members.insert(0, 'Mother-in-law')
list_of_family_members.insert(2, 'Father-in-law')
list_of_family_members.append('Brother-in-law')
for member in list_of_family_members:
    print(f'Respected {member}, I am very happy if you join the dinner on Sunday.')
print()
```

### 3.7 Shrinking Guest List
Removes guests from the list using `pop()` until only two guests remain, then displays apology messages for those removed and final invitations for the remaining guests.

```python
print('I changed my mind and will only invite 2 guests to the dinner.')
while len(list_of_family_members) > 2:
    removed_guest = list_of_family_members.pop()
    print(f'Respected {removed_guest}, sorry you are not invited to the dinner.')
print()

for member in list_of_family_members:
    print(f'Respected {member}, I am very happy if you join the dinner on Sunday.')

# Clear the remaining guests
del list_of_family_members[:]
print(list_of_family_members, '\n')
```

### 3.8 Seeing the World
Manipulates a list of locations using `sorted()`, `reverse()`, and `sort()` functions to show different arrangements without changing the original list.

```python
list_of_locations_to_visit = ['Makkah', 'Germany', 'Madinah', 'Japan', 'Canada']
print(list_of_locations_to_visit)
print(sorted(list_of_locations_to_visit))
print(list_of_locations_to_visit)
print(sorted(list_of_locations_to_visit, reverse=True))
print(list_of_locations_to_visit)

list_of_locations_to_visit.reverse()
print(list_of_locations_to_visit)
list_of_locations_to_visit.reverse()
print(list_of_locations_to_visit)

list_of_locations_to_visit.sort()
print(list_of_locations_to_visit)
list_of_locations_to_visit.sort(reverse=True)
print(list_of_locations_to_visit, '\n')
```

### 3.9 Length of List
Calculates the length of the list of locations.

```python
print(len(list_of_locations_to_visit), '\n')
```

### 3.10 Every Function
Shows various list operations like `append`, `insert`, `pop`, and `del`.

```python
knowledge_list = ['mountains', 'rivers', 'cities']
knowledge_list.append('languages')
knowledge_list.insert(0, 'religion')
print(len(knowledge_list))
print(knowledge_list)
print(knowledge_list.pop())
del knowledge_list[0]
print(knowledge_list, '\n')
```

---

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.
