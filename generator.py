def Power(max):
    for i in range(max):
        yield 2**i

stud = Power(6)

for i in stud:
    print(i)

# lst = sorted( [ (value, key) for key, value in kwargs.items()], reverse=True)