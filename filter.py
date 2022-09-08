fruits = ['apple', 'pineapple', 'lemon', 'watermelon', 'grapes', 'apricot']

filtered_fruits = filter(lambda fruit: fruit.startswith("a") == True, fruits) 
print(list(filtered_fruits))

fruits = {'apple': 40, 'watermelon': 50, 'pineapple': 20, 'graps': 30}

# print(fruits.items())

filtered = filter(lambda t: t[1]> 30, fruits.items())

print(list(filtered))