"""Bunch of functions that do square root. This is to show how to unit test"""

# All the below functions are different methods for returning the square root.
# We'll unit test to see how to identify what's failing/passing the test

def lazy_sqrt(x):
    """simplest way to get a square root"""
    return x**0.5

def builtin_sqrt(x):
    """use the math library to get the square root"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt(x):
    """Uses the Newton method to return square root"""
    val = x
    while True:
        last = val
        val = (val + x /val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val
