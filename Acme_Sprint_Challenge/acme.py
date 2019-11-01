"""Acme Product Classes"""

import random


class Product:
    """Acme Products"""

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Returns stealability by calculating price divided by weight"""
        calculation = self.price / self.weight
        if calculation < 0.5:
            return "Not so stealable..."
        elif calculation >= 0.5 and calculation < 1.0:
            return "Kinda stealable."
        else:
            return "Very Stealable!"

    def explode(self):
        """Returns explodability by multiplying flammability by weight"""
        calculation = self.flammability * self.weight
        if calculation < 10:
            return "...fizzle."
        elif calculation >= 10 and calculation < 50:
            return "..boom!"
        else:
            return "...BABMOOM!!"


class BoxingGlove(Product):
    """Product sub-class"""

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """Gloves don't explode"""
        return "...it's a glove."

    def punch(self):
        """Punch effects"""
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 < 15:
            return 'Hey that hurt!'
        else:
            return "OUCH!"
