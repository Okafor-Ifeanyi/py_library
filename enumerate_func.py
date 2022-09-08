from fileinput import filename


fruits = ['apple', 'pineapple', 'lemon', 'watermelon', 'grapes']
enum_fruit = enumerate(fruits, start=0)
print(list(enum_fruit))

# for index, element in enum_fruit:
#     filename = f"file_{index}.jpg"
#     # do something with the file and the element
#     print(filename)

names = ['Corey', 'Chirs', 'Dave', 'Travis']
enum = enumerate(names, start=0)
for index, name in enumerate(names, start=0):
    print(index, name)
 