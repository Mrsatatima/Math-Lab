#funcrions for the all calculations
from Constants import PI
class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        """
            calculates the area of a circle
            output --> returns a float
        """
        return PI*(self.radius**2)
    def circumference(self):
        """
            calculates the area of a circle
            output --> returns a float
        """
        return 2 *(PI*self.radius)
    def diameter(self):
        """
            calculates the area of a circle
            output --> returns a float
        """
        return 2 * self.radius


class Triangle:
    def __init__(self, height, base, side=None):
        self.height = height
        self.base = base
        self.side = side
    def area(self):
        """
            calculates the area of a Triangle
            output --> returns a float
        """
        return (self.height * self.base)/2
    def perimeter(self):
        """
            calculates the area of a Triangle
            output --> returns a float
        """
        return self.height + self.base + self.side

class Square:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        if self.lenght == self.width:
            return self.lenght**2
        else:
            return self.lenght * self.width
    def perimeter(self):
        if self.lenght == self.width:
            return 4 * self.lenght
        else:
            return 2*(self.lenght + self.width)

circle = Circle(6)
x = circle.area()
y = circle.diameter()
z = circle.circumference()
tri = Triangle(7,4,9)
a = tri.area()
b = tri.perimeter()
square = Square(7,7)
p = square.area()
q = square.perimeter()
print(a, b)
print(x, y, z)
print(p,q)
