import json
import csv
import time

'''
def add(a,b):
    x = a + b
    return x


def sub(a,b):
    x = a - b
    return x

x = sub(10,20)
print(x)

y = add(30,40)
print(y)
'''
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >=0:
        return x
    else:
        data = -2 + x
        return data


def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


squ = higher_order_function('absolute')



def add(a,b):
    x = a + b
    print(x)
    return x

