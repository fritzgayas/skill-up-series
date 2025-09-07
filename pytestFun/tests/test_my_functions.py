#These are function-based tests using pytest framework.
# just type in the terminal "pytest tests/test_my_functions.py" to run this test file

import pytest
import source.my_functions as my_functions  
import time

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5 #If the condition is false, an AssertionError is raised.

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

    with pytest.raises(ValueError): #Context manager to check for exceptions
        my_functions.divide(10, 0)

def test_add_strings():
    result = my_functions.add("I like using ", "pytest")
    assert result == "I like using pytest"

@pytest.mark.slow #Marking the test as slow
#To run only the slow tests, use the command: pytest -m slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_add():
    assert my_functions.add(2, 3) == 5

@pytest.mark.xfail(reason="This test is expected to fail as we know we cannot divide by zero")
def test_divide_by_zero():
    my_functions.divide(1, 0)
