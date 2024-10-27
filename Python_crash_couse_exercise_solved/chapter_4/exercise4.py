# 4.1 Pizzas

list_of_pizza : list[str] = ['italian' , 'tandori' , 'chicken tikka']
for pizza in list_of_pizza:
    print(f'I like {pizza} pizaa')
print('I really love pizza ! \n')

##############################

# 4.2 Animals

list_of_animals : list[str] = ['Goat' , 'Cow' , 'Camel']
for animal in list_of_animals:
    print(f'{animal} is good for slaughtering on the Eid')
print('We can take care of these animals in the home easily. These are not wild animals \n')

##############################

# 4.3 Counting to Twenty

for num in range(1 , 21):
    print(num)
print()

############################################

# 4.4 One Million

big_list : list[int] = [num for num in range(1 , 1000000)]
print(big_list)

#############################################

# 4.5 Summing a million

print(min(big_list))
print(max(big_list))
print(sum(big_list) , '\n')

###############################################

# 4.6 odd numbers 

for num in range(1 , 21 , 2):
    print(num)
print()

################################################

# 4.7 Threes

thress_list : list[int] = [num*3 for num in range(1 , 11)]
for num in thress_list:
    print(num)
print()

#################################################

# 4.8 & 4.9  Cubes & cube Comprehension

cubes : list[int] = [num**3 for num in range(1 , 11)]
for cube in cubes:
    print(cube)
print()

#################################################

# 4.10 Slices

cubes : list[int] = [num**3 for num in range(1 , 11)]
print('First Three items from the list')
for cube in cubes[:3]:
    print(cube)
print()

print('Three middle items from the list')
for cube in cubes[4:7]:
    print(cube)
print()

print('Three last items from the list')
for cube in cubes[-3:]:
    print(cube)
print()

#################################################

# 4.11 My Pizzas , Your Pizzas 

my_pizza : list[str] = ['italian' , 'tandori' , 'chicken tikka']
my_friend_pizza : list[str] = my_pizza[:]
my_pizza.append('Achari')
my_friend_pizza.append('crown crust')
print('My favorite Pizzas are :')
for pizza in my_pizza:
    print(pizza)
print()

print('My friend Favourite pizzas are :')
for pizza in my_friend_pizza:
    print(pizza)
print()

######################################################

# 4.13 Buffet

buffe_tuple = ('rice' , 'pizza' , 'ice-cream' , 'seekh kabab' , 'broast')
for food in buffe_tuple:
    print(food.title())
print()

buffe_tuple =('rice' , 'pizza' , 'ice-cream' , 'chicken handi' , 'kofta' )
for food in buffe_tuple:
    print(food.title())
print()





