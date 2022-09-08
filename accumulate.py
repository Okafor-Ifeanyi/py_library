from itertools import accumulate
from operator import mul

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,8,9]
result = accumulate(nums, mul)

print(list(result))

# print(list(n for n in result))

# for n in result:
#     print(n)