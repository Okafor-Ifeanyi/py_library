# Reduce Function
# Applies function of two arguments cumulatively to the items of iterable, 
# from left to right, so as to reduce the iterable to a single value.
# It's the contrary to map function.
# Extremely used in Big Data

from functools import reduce
from operator import mul

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,8,9]

digits = reduce(lambda x, y: x+y, nums, 10)

print(digits)
print(sum(nums))


# Factoral function
def factoral(n):
    return reduce(mul, range(1, n+1))

print(factoral(5))