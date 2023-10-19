import pytest
from src.example_package.example import max_search
# Pytest is the simplest test workflow ever:
#  - it works with assert
#  - all methods strating with "test_" are runned

def test_main():
    assert True

@pytest.mark.parametrize("lst", [[], [1,2,3,4,5], [1,1,1], [1,2,NaN,3]])

def test_max_search(lst):
    max = max_search()
    assert max in lst
    for i in lst:
        assert max >= i
