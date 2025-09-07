# these are class-based tests using pytest framework.
# just type in the terminal "pytest tests/test_circle.py" to run this test file
# you can also type "pytest tests/test_circle.py -v" for more verbose output
# you can also type "pytest tests/test_circle.py -s" to see print statements

import pytest
import source.shapes as shapes
import math

class TestCircle:
    def setup_method(self, method): #Setup method to initialize before each test
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10) #Create a Circle with radius 10

    def teardown_method(self, method): #Teardown method to clean up after each test
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self): #Test area method
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self): #Test perimeter method
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area() #Circle area should not equal rectangle area 