#handle exceptions

#For example if it could happen that you divide by zero
from builtins import print


def divide(number, by):
    try:
        return number/by
    except ZeroDivisionError:
        print('You cannot divide by zero')


print(divide(6,0))

#You can also have the try and except wraped around the function

number = 42
def divideby(bynumber):
    return number/bynumber

try:
    print(divideby(3))
    print(divideby(4))
    print(divideby(0))
    print(divideby(7))
except ZeroDivisionError:
    print('You cannot divide by zero wrapper')
    #once you left a try block because of an exception there is no way back:(


