# 3.1 Names 

list_of_friends_name : list[str] = ['Abdullah' , 'Muraj' , 'Arslan']
print(list_of_friends_name)
print(list_of_friends_name[0])
print(list_of_friends_name[1])
print(list_of_friends_name[2], '\n')

########################################

# 3.2 Greetings

print(f'Assalamo Alimum ! How Are you {list_of_friends_name[0]} ! Welcome to my House')
print(f'Assalamo Alimum ! How Are you {list_of_friends_name[1]} ! Welcome to my House')
print(f'Assalamo Alimum ! How Are you {list_of_friends_name[2]} ! Welcome to my House \n')

#######################################

# 3.3 Your Own List

items_list : list[str] = ['Motorcycle' , 'Laptop' , 'Car' , 'Mobile' ]
print(f'I love Honda {items_list[0]}')
print(f'I mostly used {items_list[1]}')
print(f'My aim is to buy Vezel {items_list[2]}')
print(f'My {items_list[3]} is infix smart 5 \n')

########################################

# 3.4 Guest List

list_of_family_members : list[str] = ['Mother' , 'Father' , 'Sister' , 'Brother']
print(f'Respected {list_of_family_members[0]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[1]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[2]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[3]} , I am very happy if you join the dinner on sunday \n')

########################################

# 3.5 Changing Guest List

print(f'My {list_of_family_members[3]} is busy and he can"t make the dinner')
list_of_family_members[3] = 'Uncle'
print(f'Respected {list_of_family_members[0]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[1]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[2]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[3]} , I am very happy if you join the dinner on sunday \n')

########################################

# 3.6 More Guests

print('I want to join more people on the dinner')
list_of_family_members.insert(0 , 'Mother in law')
list_of_family_members.insert(2 , 'Father in law')
list_of_family_members.append('brother in law')
print(f'Respected {list_of_family_members[0]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[1]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[2]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[3]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[4]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[5]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[6]} , I am very happy if you join the dinner on sunday \n')

###########################################

# 3.7 Shirinking Guest List

print('I change my Mind i just want to invite 2 guest on dinner')
print(f'Respected {list_of_family_members.pop(0)} sorry you not invited to the dinner')
print(f'Respected {list_of_family_members.pop(1)} sorry you not invited to the dinner')
print(f'Respected {list_of_family_members.pop()} sorry you not invited to the dinner')
print(f'Respected {list_of_family_members.pop()} sorry you not invited to the dinner')
print(f'Respected {list_of_family_members.pop()} sorry you not invited to the dinner \n')

print(f'Respected {list_of_family_members[0]} , I am very happy if you join the dinner on sunday')
print(f'Respected {list_of_family_members[1]} , I am very happy if you join the dinner on sunday')

del(list_of_family_members[0])
del(list_of_family_members[0])

print(list_of_family_members , '\n')




