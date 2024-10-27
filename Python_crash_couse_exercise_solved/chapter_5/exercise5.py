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

