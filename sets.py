# Sets
# A set is a collection which is unordered and unindexed
# Its Iterable, mutable and has no duplication elements.
# Python set class represents the mathematical notion of a set.
# The major advantage of using a set, as opposed to a list, is that has a highly optimized method for checking
# wether a specific element is contained in the set

from difflib import diff_bytes


fruits = ['apple', 'apple', 'apple', 'watermelon', 'grapes', 'grapes']
fruit_set = set(fruits)
# print(dir(fruit_set))
# print(fruit_set)

another = {'lemon', 'pineapple', 'mango', 'peach',"peach", 'grapes', "watermelon"}
print(type(another))

# Define a Set
Empty_set = set()
print(type(Empty_set))

# Add just 1 value to a set
another.add('PawPaw')

# Add more than 1 value
another.update(["coconut", "peach", "pear", "apple"])

# Remove an item from the list
# another.discard("peach")
# another.pop()

# Check super and subset
# print(fruit_set.issubset(another))
# print(another.issuperset(fruit_set))

# Union of set
# join = fruit_set | another
# print(join)

# Difference
print(another.difference(fruit_set))

# Symetric Difference
print(another.symmetric_difference(fruit_set))


# print(fruit_set)
# print(another)

Empty_set.update([1,2,3,5,1,2,4])
print(Empty_set)

# Frozen set