# Closures
# There are 3 things that we need in order to have a closure:
# 1. We must have a nested function
# 2. The nested function must refer to a value defined in the enclosing function 
# 3. The enclosing function must return the nested function


from email import message


def print_message(msg):
    def printer():
        nonlocal msg
        msg += " world!"
        print(msg)
    return printer

another_function = print_message('Hello')
 
# another_function()

del print_message

# another_function = print_message('Hello')
another_function()


# Closures can avoid the use of global values
# Provides some form of data hiding.
# It can provide an object oriented solution to the problem.
# Decorators!

class Multiplier:
    def __init__(self, n, x):
        self.n = n
        self.x = x
    def multiply(self):
        return self.x*self.n

obj = Multiplier(5,7)
print(obj.multiply())

def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()
my_func()
my_func()
my_func()
my_func()