"""Writing functions to work with arrayss and strings"""

import string
import numpy as np

def increment(x):
    """adds one to x"""
    return(x+1)

def strip_punctuation(text):
    """Strips out punctuation"""
    exclude = string.strip_punctuation
    return ''.join(s for s in text if s not in exclude)
