import pytest
import numpy as np
from example_package.example import max_search
# Pytest is the simplest test workflow ever:
#  - it works with assert
#  - all methods strating with "test_" are runned

def test_main():
    assert True

@pytest.mark.parametrize("cases", [([], float('nan')),
                                 ([1,2,3,4,5], 5),
                                 ([1,1,1], 1),
                                 ([1,2,float('nan'),3], float('nan'))])
def test_max_search(cases):
    lst, result = cases
    max = max_search(lst)
    # Check the weird cases
    if np.isnan(max):
        assert np.isnan(lst).any() or not lst
    # Check classics
    else:
        assert max in lst
        assert max == result
        for i in lst:
            assert max >= i
