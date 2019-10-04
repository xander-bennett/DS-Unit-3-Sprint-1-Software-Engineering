# Will need to import Product class from acme.py
# Hey cool, i'm importing my own stuff
from acme import Product
from random import sample, randint, uniform

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    """ Generate a list of ACME products """
    products = []
    for i in range(num_products):
        name = ADJECTIVES[randint(0, 4)] + ' ' + NOUNS[randint(0, 4)]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):
    """ Print a report for a list of products """
    names = set(list(i.name for i in products))
    avg_price = sum(i.price for i in products) / len(products)
    avg_weight = sum(i.weight for i in products) / len(products)
    avg_flammability = sum(i.flammability for i in products) / len(products)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT\n")
    print('Unique names - ', len(names))
    print('Average weight - ', avg_weight)
    print('Average price - ', avg_price)
    print('Average flammability - ', avg_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
