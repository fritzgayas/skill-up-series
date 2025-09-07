import math

class Shape: #We will use this for inheritance
    def area(self):
        pass

    def perimeter(self):  
        pass

class Circle(Shape): #This inherit from Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2) #Pi times radius squared

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius #2 Pi R
    

class Rectangle(Shape): #This inherit from Shape
    def __init__(self, width, length): #Initialize with width and height
        self.width = width
        self.length = length

    def __eq__(self, other): #Equality check based on width and height
        if not isinstance(other, Rectangle): #If it is not Rectangle, return False
            return False
        
        return self.width == other.width and self.length == other.length

    def area(self):
        return self.width * self.length #Width times Height

    def perimeter(self):
        return 2 * (self.width + self.length) #2 times (Width + Height)
    
class Square(Rectangle): #Square is a special case of Rectangle, so we inherit from Rectangle
    def __init__(self, side_length):
        super().__init__(side_length, side_length) #Call the parent class (Rectangle) constructor with equal width and length 