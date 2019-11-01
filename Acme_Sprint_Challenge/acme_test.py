import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_flammability(self):
        """Test default flammability being 0.5"""
        prod = Product('Test Flammability')
        self.assertEqual(prod.flammability, 0.5)

    def test_explode_stealability(self):
        """Test sample product stealability/explode"""
        prod = Product('Test', price = 15, weight = 5.0, flammability = 1.0)
        self.assertEqual(prod.stealability(), "Very Stealable!")
        self.assertEqual(prod.explode(), "...fizzle.")


if __name__ == '__main__':
    unittest.main()
