# 8.1 Message

def display_message():
    """
    Program about what we learn in this chapter
    """
    print('This chapter is about user defined functions \n')

display_message()

###############################################

# 8.2 Favorite Book

def favorite_book(title : str):
    print(f'My favourite books is {title.title()} \n')

favorite_book('quran majeed')

################################################

# 8.3 T-shirt

def make_shirt(size : str , text : str):
    print(f'Your shirt size is : {size} and you want to write : {text} \n')

make_shirt('medium' , 'i love you')
make_shirt(text = 'Pakistan Zindabad' , size = 'small')

################################################

# 8.4 Large Shirts

def make_shirt(size : str = 'large' , text : str = 'I love Python'):
    print(f'Your shirt size is : {size} and you want to write : {text} \n')

make_shirt()
make_shirt(size = 'Medium')
make_shirt(text = 'I love Imran Khan' )

###############################################

# 8.5 Cities

def describe_city(city : str , country : str = 'Pakistan'):
    print(f'{city.title()} in {country.title()} \n')

describe_city('rawalpindi' )
describe_city('lahore')
describe_city('new york' , country = 'America')

#################################################

# 8.6 City Names

def city_country(city : str , country : str):
    senetence : str = f"{city} , {country}"
    return senetence.title()

one = city_country('rawalpindi' , 'pakistan')
two = city_country('makkah' , 'saudia arabia')
three = city_country('lahore' , 'pakistan')
print(one,'\n',two,'\n',three)

############################################

# 8.7 Album

def make_album(artist_name : str  , album_title : str , number_of_songs : int = None):
    album = {'Artist_Name' : artist_name , 'Album_Title' : album_title} 
    if number_of_songs:
        album['num_of_songs'] = number_of_songs

    return album

album1 = make_album('Ali' , 'Tara zameen per')
album2 = make_album('Farhan' , 'Ham sab 1 Hain')
album3 = make_album('Farooq' , 'Laggan')
album4 = make_album('kiran' , 'Khobsorti' , 5)

print(f'{album1} \n {album2} \n {album3} \n {album4}')

################################################

# 8.7 User Albums


def make_album(artist_name: str, album_title: str, number_of_songs: int = None) -> dict:
    album = {'Artist_Name': artist_name, 'Album_Title': album_title}
    if number_of_songs:
        album['num_of_songs'] = number_of_songs
    return album

while True:
    ar_name = input('Enter the artist name (or "q" to quit at any time): \n')
    if ar_name.lower() == 'q':
        break
    
    al_title = input('Enter the album title (or "q" to quit at any time): \n')
    if al_title.lower() == 'q':
        break
    
    nu_songs = input('Enter the number of songs (or "q" to quit at any time): \nq')
    if nu_songs.lower() == 'q':
        break
    
    # Convert `nu_songs` to an integer if provided
    if nu_songs.isdigit():
        nu_songs = int(nu_songs)
    else:
        nu_songs = None  # Set to None if not provided or not a digit

    # Create the album dictionary using the user inputs
    album = make_album(ar_name, al_title, nu_songs)
    print(f"\nAlbum details: {album}\n")

####################################################

# 8.9 Messages

def show_messages(messages : list):
    for mess in messages:
        print('\n' , mess , '\n')

mess_list : list[str] = [
    'My name is Hamza Atiq',
    'I am a student of PIAIC',
    'My aim is to become a AI developer',
    'I will run a software house in a next 5 years Insha Allah'
] 

show_messages(mess_list)

####################################################

# 8.10 Sending Messages

def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    """
    Prints each message from the messages list and moves it to the sent_messages list.
    """
    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.append(message)

# Lists for messages to be sent and already sent messages
sent_message_list: list[str] = []
mess_list: list[str] = [
    'My name is Hamza Atiq',
    'I am a student of PIAIC',
    'My aim is to become an AI developer',
    'I will run a software house in the next 5 years, Insha Allah'
]

# Call the function to send messages
send_messages(mess_list, sent_message_list)

# Print both lists to verify the messages were moved
print("\nOriginal messages list (should be empty):", mess_list , '\n')
print("Sent messages list (should contain all messages):")
for message in sent_message_list:
    print(message)
print()

############################################

# 8.11 Archived Messages

def send_messages(messages: list[str], sent_messages: list[str]) -> None:
    """
    Prints each message from the messages list and moves it to the sent_messages list.
    """
    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.append(message)

# Lists for messages to be sent and already sent messages
sent_message_list: list[str] = []
mess_list: list[str] = [
    'My name is Hamza Atiq',
    'I am a student of PIAIC',
    'My aim is to become an AI developer',
    'I will run a software house in the next 5 years, Insha Allah'
]

# Call the function to send messages
send_messages(mess_list[:], sent_message_list)

# Print both lists to verify the messages were moved
print("\nOriginal messages list (not  empty):", mess_list , '\n')
print("Sent messages list (should contain all messages):")
for message in sent_message_list:
    print(message)
print()

#################################################

# 8.12 Sandwiches 

def sandwiches(*sandwich_orders: str) -> None:
    """
    Accepts any number of sandwich ingredients and prints a summary of the sandwich being ordered.
    """
    print("The following items have been added to your sandwich:")
    for item in sandwich_orders:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

# Calling the function three times with a different number of arguments each time
sandwiches('Tuna', 'Avocado', 'Egg', 'Pastrami')
sandwiches('Egg', 'Mayonnaise', 'Ketchup')
sandwiches('Sauce', 'Olives', 'Butter')

########################################################

# 8.13 User profile

def build_profile(first : str  , last : str , **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = build_profile('hamza' , 'atiq' , education = 'Bsc' , location = 'rawalpindi', 
                             hobby = 'coding')
print(user_profile , '\n')

###########################################

# 8.14 Cars

def make_car(manufacturer: str, model_name: str, **car_data) -> dict:
    """
    Builds a dictionary containing details about a car.
    
    Parameters:
    - manufacturer (str): The manufacturer of the car.
    - model_name (str): The model name of the car.
    - **car_data: Arbitrary keyword arguments representing additional car information.
    
    Returns:
    - dict: A dictionary with all the information about the car.
    """
    # Create the base dictionary with manufacturer and model
    car_info = {
        'manufacturer': manufacturer.title(),
        'model_name': model_name.title()
    }
    
    # Add any additional information provided in car_data
    car_info.update(car_data)
    
    return car_info

# Call the function with required and additional keyword arguments
car1 = make_car('suzuki', 'old version', owner_name='Uzair', year_of_purchasing='2019',
                color='grey', tow_package=True)

# Print the dictionary to verify that information was stored correctly
print(car1)
