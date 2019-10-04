import unittest
from acme import Product
from acme_report import generate_products, inventory_report, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ test product weight being 20 """
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealable_explosive(self):
        """ Testing stealability and explosiveness """
        prod = Product('Test', price=15, flammability=50000)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    """ Test Acme Report """

    def test_default_num_products(self):
        """ Test that the default num_products is correct. """
        items = generate_products()
        self.assertEqual(len(items), 30)

    def test_legal_names(self):
        """ Test that generated product names are legal. """
        items = generate_products()
        adjectives = list(i.name.split(' ')[0] for i in items)
        nouns = list(i.name.split(' ', 1)[1] for i in items)
        for i in adjectives:
            self.assertIn(i, ADJECTIVES)
        for i in nouns:
            self.assertIn(i, NOUNS)

if __name__ == '__main__':
    unittest.main()
