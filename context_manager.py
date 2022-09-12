# f = open('sample.txt', 'w')
# f.write("lorem ipsu dolor sit amet, consectetur adipiscing elit.")
# f.close()

# with open('sample.txt', 'w') as f:
#     f.write('lorem ipsu dolor sit amet, consectetur adipiscing elit.')

# class Open_File():

#     def __init__(self, filename, mode) -> None:
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()

# with Open_File('sample.txt', 'w') as f:
#     f.write('chidinma Mood swing')

# print(f.closed) 

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('Chidinma Mood swing')

print(f.closed)