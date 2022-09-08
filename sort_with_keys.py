# Sort only works for list
# Sorted function works for any Iterable
# You can specify reverse in both of them
# Specify Key

fruits = {'apple': 40, 'watermelon': 50, 'pineapple': 20, 'graps': 30}
fruits_list = ['apple', 'pineapple', 'lemon', 'watermelon', 'grapes']

# Sorts the list out here and modifys argument
# fruits = list(fruits)

# Sorts the list and does not modify argument
print(sorted(fruits))
print(sorted(fruits.keys()))
print(sorted(fruits.values()))

# sorts the by values but gets keys
print(sorted(fruits, key=lambda fruit: fruits[fruit], reverse=True))
