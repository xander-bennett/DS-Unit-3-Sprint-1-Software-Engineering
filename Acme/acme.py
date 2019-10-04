"""Classes to represent products"""

from random import random
from random import randint
import random

class Product:
    """ General representation of an acme product """

    def __init__(self, name, price = 10, weight = 20, flammability = 0.5,
    identifier = random.randint(1000000,9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Divides price by weight. Ratios return stealability strings """
        if (self.price / self.weight) < 0.5:
            print('Not so stealable...')
        elif (self.price / self.weight) >= 0.5 < 1.0:
            print('Kinda stealable.')
        else: print('Very stealable!')

    def explode(self):
        """ Calculates flammabiliy * weight, returns explosion size """
        if (self.flammability * self.weight) < 10:
            print('...fizzle')
        elif (self.flammability * self.weight) >= 10 < 50:
            print('...boom!')
        else: print('...BABOOM!')

class BoxingGlove(Product):
    """BoxingGlove Sublcass"""
    def __init__(self, name, price=10, weight=10, flammability=0.5,
     identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        """Prints what will happen if the product is too flammable"""
        print("it's a glove.")

    def punch(self):
        """Prints what happens when boxing glove punches someone."""
        if self.weight < 5:
            print('That tickles.')
            return
        elif self.weight >= 5 < 15:
            print('Hey that hurt!')
            return
        else:
            print("OUCH!")
            return
    pass
