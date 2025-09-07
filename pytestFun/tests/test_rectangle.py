#Topic on fixtures
#A fixture is a function that sets up some context for tests
#Fixtures are used to provide a fixed baseline upon which tests can reliably and repeatedly execute

import pytest

def test_area(my_rectangle):
    assert my_rectangle.area() == 20 #Area should be 4 * 5 = 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 18 #Perimeter should be 2 * (4 + 5) = 18

def test_not_equal(my_rectangle, unusual_rectangle):
    assert my_rectangle != unusual_rectangle #These two rectangles should not be equal
 