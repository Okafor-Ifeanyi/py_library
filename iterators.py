# # Iterable is a representation of a series of elements that can't be iterated over eg list, dict, strings
# # but dont have an iteration state such as current element, every iterable can be converted to an iterator by using
# # An Iter, an iterable should be able to produce any number of iterator
# # Iterator, Object with iteration state. Helps u check d next using __next__() or next() 

# from unittest import result


# fruits = ['apple', 'pineapple', 'lemon', 'watermelon', 'grapes', 'apricot']

# fruits.sort()
# fruits = iter(fruits)
# # print(next(fruits))


# while True:
#     try:
#         element = next(fruits)
#         # print(element)
#     except StopIteration:
#         break

# class Powers:
#     def __init__(self, max=0):
#         self.maximum = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= self.maximum:
#             result = 2**self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration

# obj = iter(Powers(5))

# # print(next(obj))
# # print(next(obj))   
# # print(next(obj))   
# # print(next(obj))   
# # print(next(obj))   
# # print(next(obj))   
# # print(next(obj))   

# nums = [1, 2, 3]

# # i_nums = nums.__iter__()
# i_nums = iter(nums)

# while True:
#     try:
#         element = next(i_nums)
#         print(element)
#     except StopIteration:
#         break

# # for num in nums:
# #     print(num)

# print(dir(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

# Generator function

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

# print(nums)
count = 0
for num in nums:
    count += 1
    # if count > 4:
    #     break
    print(num)
