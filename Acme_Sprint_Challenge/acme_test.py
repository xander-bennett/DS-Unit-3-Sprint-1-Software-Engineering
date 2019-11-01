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
        prod = Product('Test', price=15, weight=5.0, flammability=1.0)
        self.assertEqual(prod.stealability(), "Very Stealable!")
        self.assertEqual(prod.explode(), "...fizzle.")


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """Test the default number of products in the report"""
        i = generate_products()
        self.assertEqual(len(i), 30)

    def test_legal_names(self):
        """Test that product names are as expected"""
        products = generate_products()
        adjectives = list(i.name.split(' ')[0] for i in products)
        nouns = list(i.name.split(' ', 1)[1] for i in products)
        for i in adjectives:
            self.assertIn(i, ADJECTIVES)
        for i in nouns:
            self.assertIn(i, NOUNS)


if __name__ == '__main__':
    unittest.main()
