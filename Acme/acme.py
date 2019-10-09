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
        value_weight_ratio = self.price/ self.weight
        if value_weight_ratio < 0.5:
            return 'Not so stealable...'
        elif value_weight_ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """ Calculates flammabiliy * weight, returns explosion size """
        boom_ratio = self.flammability * self.weight
        if boom_ratio < 10:
            return '...fizzle'
        elif boom_ratio < 50:
            return '...boom!'
        else:
            return '...BABOOM!'

class BoxingGlove(Product):
    """BoxingGlove Sublcass"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "it's a glove."

    def punch(self):
        """Prints punching effects"""
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 < 15:
            return 'Hey that hurt!'
        else:
            return "OUCH!"
