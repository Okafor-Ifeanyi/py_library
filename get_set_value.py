
fruits = {'apple': 40, 'watermelon': 50, 'pineapple': 20, 'graps': 30}

print(fruits.get("pineapple"))

# Only adds if value doesnt exist
fruits.setdefault("apple", 0)

print(dir(fruits))

print(fruits) 

quantites = dict()
for fruit in fruits:
    quantites[fruit] = quantites.get(fruit, 0) + 1

print(quantites)