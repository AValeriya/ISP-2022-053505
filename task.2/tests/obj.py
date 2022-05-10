import math

c = 42           #global peremennaya


class Cocktail:
    def __init__(self, taste, volume):
        self.taste = taste
        self.volume = volume
        self.ttuple = ('coconut', 'chocolate', 'strawberry')
        self.additives = ['coconut', 'chocolate', 'strawberry']    #list
        self.price = {'cheap': 'true'}                             #dict


def f(x):
    a = 123
    #return x*a*c
    return math.sin(x * a * c)