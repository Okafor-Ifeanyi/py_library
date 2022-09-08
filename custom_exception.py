from ast import Num
from logging import exception
import random
from tokenize import Number

correct_number = random.randint(1, 1000)

class Numbertoosmall(Exception):
    pass

class Numbertoobig(Exception):
    pass

guess = 10
while guess > 0:
    print(f'You have {guess} left')
    try:
        num = int(input("Enter your Number: "))
        if num < correct_number:
            raise Numbertoosmall('The number is too small')
        elif num > correct_number:
            raise Numbertoobig('THe number is too big')
        else:
            print(f"{num} is the correct number")
            break
    except Numbertoosmall as error:
        print(error)
    except Numbertoobig as error:
        print(error)
    except ValueError:
        print("You need to enter an int")

    guess -= 1