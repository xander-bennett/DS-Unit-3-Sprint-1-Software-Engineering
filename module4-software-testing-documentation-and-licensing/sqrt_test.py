"""This is our testing file for square root functions"""
import unittest
# Importing the sqrt.py folder to be unit tested
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt
# Our class for square root functions
class SqrtTests(unittest.TestCase):
    """These are our tests for square root funcs"""
    # This method below is testing the abilit of the lazy_sqrt to do what we want
    # by 'saying' that it passes the test if the lazy_sqrt function we built
    # will return a 3 if we plug a 9 into the function.
    # We test by running the test file in python with $ python sqrt_test.py
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)
    # This next one uses the 'AlmostEqual' method because the square root isn't a whole number.
    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt(2),1.4142135623730949998)
        # Note. this may fail pytest because pytest is precise up to like 15 characters

class OtherTests(unittest.TestCase):
    def test_thing(self):
        pass

# This piece of code has to be at the end of your _test.py file to run the unit test
if __name__ == '__main__':
    unittest.main()
