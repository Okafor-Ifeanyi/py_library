# The Counter Class 
# A counter is a dict for counting hashable object. it is collection where elements are stored as dictionary
# keys and their counts are stored as dictionary values.
# Counts are allowed to be any integer value including zero or negative courts. The counter class is similar to bags 
# or multisets in other languages.
# Elements are counted from an iterable or initialized from another mapping(or counter).

from collections import Counter

fruits = ["apple", "apple", "apple", "watermelon", "grapes", "grapes"]

counts = Counter(fruits)
counts.setdefault("apples", 0)

# print(dir(counts))
print(counts.most_common(3))
print(fruits)
print(Counter("mississipi"))