
# Python Exercises - Book Chapter 4

Welcome to my GitHub repository for Python exercises. Here, I practice and share code snippets from my journey through a Python book. Each script is organized by exercise number and includes tasks that improve basic Python skills like list operations, loops, and comprehensions.

## Table of Contents
1. [4.1 Pizzas](#41-pizzas)
2. [4.2 Animals](#42-animals)
3. [4.3 Counting to Twenty](#43-counting-to-twenty)
4. [4.4 One Million](#44-one-million)
5. [4.5 Summing a Million](#45-summing-a-million)
6. [4.6 Odd Numbers](#46-odd-numbers)
7. [4.7 Threes](#47-threes)
8. [4.8 & 4.9 Cubes](#48--49-cubes--cube-comprehension)
9. [4.10 Slices](#410-slices)
10. [4.11 My Pizzas, Your Pizzas](#411-my-pizzas-your-pizzas)
11. [4.13 Buffet](#413-buffet)

---

### 4.1 Pizzas
The program iterates over a list of favorite pizzas and prints statements about each one.

```python
list_of_pizza = ['italian', 'tandori', 'chicken tikka']
for pizza in list_of_pizza:
    print(f'I like {pizza} pizza')
print('I really love pizza!\n')
```

### 4.2 Animals
This script lists animals suitable for Eid, and each animal is described in terms of its usefulness.

```python
list_of_animals = ['Goat', 'Cow', 'Camel']
for animal in list_of_animals:
    print(f'{animal} is good for slaughtering on Eid')
print('We can take care of these animals in the home easily. These are not wild animals.\n')
```

### 4.3 Counting to Twenty
A simple loop to print numbers from 1 to 20.

```python
for num in range(1, 21):
    print(num)
print()
```

### 4.4 One Million
Generates a list of numbers from 1 to 1,000,000. This demonstrates the use of Python’s range function and handling large sequences (commented out to prevent excessive output).

```python
# big_list = [num for num in range(1, 1000000)]
# print(big_list)
```

### 4.5 Summing a Million
Finds the minimum, maximum, and sum of a list containing numbers from 1 to 1,000,000. This is useful for learning list aggregation functions.

```python
# print(min(big_list))
# print(max(big_list))
# print(sum(big_list), '\n')
```

### 4.6 Odd Numbers
Prints all odd numbers between 1 and 20. This exercise shows how to use `range()` with a step argument to skip numbers.

```python
for num in range(1, 21, 2):
    print(num)
print()
```

### 4.7 Threes
Creates a list of the first ten multiples of 3, then prints each item.

```python
threes_list = [num * 3 for num in range(1, 11)]
for num in threes_list:
    print(num)
print()
```

### 4.8 & 4.9 Cubes
Generates a list of the cubes of numbers from 1 to 10, then prints each item. This demonstrates list comprehension and exponentiation.

```python
cubes = [num ** 3 for num in range(1, 11)]
for cube in cubes:
    print(cube)
print()
```

### 4.10 Slices
Displays slices of a list containing cubes. Shows the first three items, three middle items, and three last items of the list.

```python
cubes = [num ** 3 for num in range(1, 11)]
print('First three items from the list:')
for cube in cubes[:3]:
    print(cube)
print()

print('Three middle items from the list:')
for cube in cubes[4:7]:
    print(cube)
print()

print('Three last items from the list:')
for cube in cubes[-3:]:
    print(cube)
print()
```

### 4.11 My Pizzas, Your Pizzas
Copies a list of favorite pizzas, adds unique pizzas to each list, and then prints each list to show how lists can be independently modified even after copying.

```python
my_pizza = ['italian', 'tandori', 'chicken tikka']
my_friend_pizza = my_pizza[:]
my_pizza.append('Achari')
my_friend_pizza.append('Crown Crust')
print('My favorite pizzas are:')
for pizza in my_pizza:
    print(pizza)
print()

print('My friend\'s favorite pizzas are:')
for pizza in my_friend_pizza:
    print(pizza)
print()
```

### 4.13 Buffet
Defines a tuple of food items available at a buffet, prints each item, and then redefines the tuple to show how tuples (immutable sequences) can be re-assigned.

```python
buffet_tuple = ('rice', 'pizza', 'ice-cream', 'seekh kabab', 'broast')
for food in buffet_tuple:
    print(food.title())
print()

buffet_tuple = ('rice', 'pizza', 'ice-cream', 'chicken handi', 'kofta')
for food in buffet_tuple:
    print(food.title())
print()
```

---

### Getting Started
To run these exercises, you need Python 3 installed. Each script is standalone, so you can run them individually by executing `python filename.py` in your terminal.

### Author
**Hamza Atiq**  
Passionate about learning Python and coding practices.

### Acknowledgments
Thanks to the authors of the Python book that inspired these exercises.

