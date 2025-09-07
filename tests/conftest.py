#Conftest.py is short for configuration for tests
#A conftest.py in one folder applies only to test files in that folder and its subfolders.
#This is where we define our rectangles
#You make objects globally available to all test files by putting it in conftest.py

import pytest
import source.shapes as shapes

@pytest.fixture #This is helpful to create a rectangle object for tests
def my_rectangle():
    return shapes.Rectangle(4, 5) #Create a Rectangle with width 4 and length 5

@pytest.fixture #A fixture for a different rectangle
def unusual_rectangle():
    return shapes.Rectangle(5, 6) #Create a Rectangle with width 5 and length 6