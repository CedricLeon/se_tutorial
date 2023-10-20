import numpy as np


def hello_world():
    print("hello world")

def max_search(lst):
    # Check if list is empty or contains any 'nan'
    if not lst or np.isnan(lst).any():
        return float('nan')

    return np.max(lst)
