import numpy as np
def hello_world():
    x = np.zeros(5)
    print("hello world")

def max_search(lst):
    # Check if list is empty
    if not lst or np.isnan(lst).any():
        return float('nan')

    return np.max(lst)
