# Will need to import Product class from acme.py
# Hey cool, i'm importing my own stuff
from acme import Product
from random import sample, randint, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']




def __init__(self, num_product=30, products=None, products_set=None):
    super().__init__()

    self.num_product = num_product
    self.products = products
    self.products_set = products_set

def generate_products(self,num_product=30):
    """Random Generator of total product number"""
    self.products = [' '.join(sample(ADJECTIVES, 1) + sample(NOUNS, 1))
                    for _ in range(num_product)]
    self.products_set = set(self.products)
    self.products = len(self.products_set)

    print("Unique product names:", self.products)

    return

def inventory_report(self, products):
    """Average characteristics of listed products"""
    avg_price = self.price / products
    print('Average price:', avg_price)

    avg_weight = self.weight / products
    print('Average weight:', avg_weight)

    avg_flammability = self.flammability / products
    print('Average flammability:', avg_flammability)

    return
pass

if __name__ == "__main__":
    inventory_report(generate_products())
