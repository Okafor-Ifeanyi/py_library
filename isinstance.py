# The isinstance() function returns True if the specified object 
# is of the specified type, otherwise False.

# isinstance(object, type)

x = isinstance(5, int)
print(x)

# check if y and r are instances of a class
class myObj:
    name = "John"

y = myObj()
r = "John"

x = isinstance(r, myObj)
print(x)