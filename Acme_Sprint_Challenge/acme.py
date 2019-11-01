"""Acme Product Classes"""

import random

class Product:
    """Acme Products"""

    def __init__(self, name, price = 10, weight = 20, flammability = 0.5,
    identifier = random.randint(1000000,9999999)):
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
