import numpy as np


def hello_world():
    print("hello world")


def max_search(lst):
    """Search for the maximum of a list.
    Parameters
    ----------
    lst : list
        list to be browsed.
    Returns
    -------
    float :
        Max of the list or float('nan') if the list is empty or contains a float('nan').
    """
    # Check if list is empty or contains any 'nan'
    if not lst or np.isnan(lst).any():
        return float('nan')

    return np.max(lst)

if __name__ == "__main__":
    hello_world()
