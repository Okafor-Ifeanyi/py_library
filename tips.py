# Enumerate to get index
import abc
from ast import Pass


names = ['Corey', 'Chirs', 'Dave', 'Travis']
enum = enumerate(names, start=0)
# print(dict(enum))
# print(list(enum))

# for index, name in enumerate(names, start=0):
    # print(index, name)



# looping over 2 lists
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# print(dict(zip(names, heros)))

# for names, hero in zip(names, heros):
#     print(f"{names} is actually {hero}")



# Unpacking
a, b, *c, d, e, f = (1,2,3,4,5)

# print(a)
# print(b)
# print(c)



# Used in switching d placement of variables
# setattr()

class Person():
    pass

person = Person()

first_key = 'First'
first_val = "Bio"

# setattr(person, first_key, first_val)

# first = getattr(person, first_key)

# print(first)

# person_info = {'first': 'Prog', 'last': 'BIO'}

# for key, value in person_info.items():
#     setattr(person, key, value)

# for key in person_info.keys():
#     print(getattr(person, key)) 



# Hiding password
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
print(password) 