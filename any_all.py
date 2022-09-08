# Any 
# returns True and False otherwise
# At least one value is True => True
# All values are False => False
# Empty Iterable => False

fruits = ["apple", "pineapple", "lemon", "watermelon", "avocado"]
# fruit_map = map(lambda fruit: fruit.endswith("apple"), fruits)
fruit_map = map(lambda fruit: len(fruit) > 1, fruits)
print(any(fruit_map))
# print(list(fruit_map))


# All
# Return True if all elements of an iterable is True and False otherwise
# At least one value is False => False
# All values are True => True
# Empty Iterable => True

fruits_mapped = map(lambda fruit: len(fruit) < 50, fruits)
print(all(fruits_mapped))
