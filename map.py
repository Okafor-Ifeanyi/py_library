# Retruns a map function to each item of an iterable
# Returns a map object
# Use it instead of loops whenever you can

fruits = ['apple', 'pineapple', 'lemon', 'watermelon', 'grapes']

result = list()
for fruit in fruits:
    result.append(fruit.capitalize())
print(result)

# Map function

def process(fruit):
    resulting_string = fruit.capitalize()
    if fruit.endswith('s'):
        resulting_string += ' are great!'
    else:
        resulting_string += ' is great!'
    return resulting_string

result = map(process, fruits)
print(list(result))
