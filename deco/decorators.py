# Decorators - In python you can pass functions as arguments
# to other functions. Such functions are called Higher Order Functions (HOF)
# HOF can return functions, as we saw closures
# Decorators is simple terms, takes a function, adds some extra functionalities and returns it.
# 

from logger import my_logger
import time


def wrapper(f):
    def inner():
        print("I am a docorated function")
        f()
    return inner

@wrapper
def hello_world():
    print("Hello World")

# print(hello_world())

def wrapper(f):
    def inner(a,b):
        if b == 0:
            print('We cannot use b as zero')
            return
        else:
            return f(a, b)
    return inner

@wrapper
def divide(a, b):
    return a/b

# print(divide(3,4)) 

def wrapper(f):
    def inner(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        execution_time = end-start
        print(f"This function took {execution_time} seconds")
    return inner

@wrapper
def complicated_operation(a,b,c):
    r = a+b+c
    r *= a
    r /= c
    print(r)

print(complicated_operation(9,9,6))
print("\n ")


# Decorator function method
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

# Decorator class method 
class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('Display function ran')

@my_logger
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display()
display_info('BIO', 21)