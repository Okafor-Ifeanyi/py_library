# *args and **kwargs
# we can pass a var number of arguments to a function using:
# *args(non-keyword arguments)
# **kwargs (keyword arguments) 



# *args allows me to pass a var number of parameters, which will be encapsulated in a tuple
from ast import arg
from audioop import reverse


def add(*args):
    print(args[0])
    return len(args) 

add = add(1,34,6,4,23,89,5,0,2)
print(add)

# python can pass a variable num of keywords arguments **kwargs
def print_fruits(**kwargs):
    # print(dir(kwargs))

    # for key, value in kwargs.items():
    # #     dict = (value, key)
    #     sorted = dict.sort()
    # #     print(sorted)

    # List comprehension
    
    lst = sorted( [ (value, key) for key, value in kwargs.items() ], reverse=True)

    for value, key in lst:
        (key,value)

def sort_list(**kwargs):
    sorted = kwargs.sort()
    print(sorted)
        

print_fruits(apple=60, pineaple=40, lemon=20, watermelon=10, grapes=200)
# sort_list(apple=60, pineaple=40, lemon=20, watermelon=10, grapes=200)
