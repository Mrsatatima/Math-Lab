#funcrions for the all calculations
from Constants import PI
class Geometry:
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
                """
                    calculates the area of a Square
                    output --> returns a float
                """
                if self.lenght == self.width:
                    return self.lenght**2
                else:
                    return self.lenght * self.width
            def perimeter(self):
                """
                    calculates the perimeter of a Square
                    output --> returns a float
                """
                if self.lenght == self.width:
                    return 4 * self.lenght
                else:
                    return 2*(self.lenght + self.width)

        class Trapezium:
            def __init__(self, baseA, baseB, height=1, side=None):
                self.height = height
                self.baseA = baseA
                self.baseB = baseB
                self.sideA = height
                self.sideB = side
            def area(self):
                """
                    calculates the area of a Trapezium
                    output --> returns a float
                """
                return self.height * (self.baseA + self.baseB)/2
            def perimeter(self):
                """
                    calculates the perimeter of a Trapezium
                    output --> returns a float
                """
                return float(self.baseA + self.baseB + self.sideA + self.sideB)

        class Parallelogram:
            def __init__(self, base, height,):
                self.base = base
                self.height = height
                self.side = height
            def area(self):
                """
                    calculates the area of a Parallelogram
                    output --> returns a float
                """
                return float(self.base * self.height)

            def perimeter(self):
                """
                    calculates the perimeter of a Parallelogram
                    output --> returns a float
                """
                return 2 *(self.side + self.base)

        class Cube:
            def __init__(self, lenght, width, height):
                self.lenght = lenght
                self.width = width
                self.height = height
            def volume (self):
                if self.width == self.height == self.lenght:
                    return self.width**3
                else:
                    return self.width * self.height * self.lenght
            def surface_area(self):
                if self.width == self.height == self.lenght:
                    return 6 *self.width**2
                else:
                    return 2*((self.width * self.height) + (self.height* self.lenght) + (self.width* self.lenght))

        class Sphere:
            def init(self, radius):
                self.radius = radius
            def volume(self):
                return (4/3) * PI * radius ** 3
            def surface_area(self):
                return 4 * PI * radius **2

        class Cylinder:
            def __init__(self, radius, height):
                self.radius = radius
                self.height = height
            def volume(self):
                return PI * (self.radius**2) * self.height
            def surface_area(self):
                return 	2(PI * self.radius**2) + 2 * PI * self.radius * self.height

        class Cone:
            def __init__(self, radius, height):
                self.radius = radius
                self.height = height
                self.side = height
            def volume(self):
                return (1/3) * PI * self.radius * self.height
            def surface_area(self):
                return PI * radius * self.side
