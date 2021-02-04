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
            def __init__(self, radius):
                self.radius = radius
            def volume(self):
                return (4/3) * PI * self.radius ** 3
            def surface_area(self):
                return 4 * PI *self.radius **2

        class Cylinder:
            def __init__(self, radius, height):
                self.radius = radius
                self.height = height
            def volume(self):
                return PI * (self.radius**2) * self.height
            def surface_area(self):
                return 	 2 * (PI * self.radius) * self.height + 2*PI * (self.radius**2)

        class Cone:
            def __init__(self, radius, height):
                self.radius = radius
                self.height = height
                self.side = height
            def volume(self):
                return (1/3) * PI * self.radius * self.height
            def surface_area(self):
                return PI * radius * self.side

class Conversion:
    class Lenght:
        def __init__(self, value, frm, to):
            self.value = value
            self.frm = frm
            self.to = to
            self.conversion_value = {"cm,km":100000, "cm,m":100, "cm,ft": 30.48, "m,km":1000,
                                     "mm,ft":304.8,"mm,cm":10, "mm,m": 1000, "mm,km":1000000,
                                     "ft,m":3.2808, "ft,km":3280.84, "mm,yd":914.4, "cm,yd":91.44,
                                     "yd,m":1.09361, "yd,km":1093.613298}
        def converter(self):
            for unit, value in self.conversion_value.items():
                if self.frm == unit.split(",")[0] and self.to == unit.split(",")[1]:
                    return self.value/value
                elif self.to == unit.split(",")[0] and self.frm == unit.split(",")[1]:
                    return self.value*value
    class Volume:
        def __init__(self, value, frm, to):
            self.value = value
            self.frm = frm
            self.to = to
            self.conversion_value = {"ml,l":1000, "ml,m3":1000000, "l,m3":1000}
        def converter(self):
            for unit, value in self.conversion_value.items():
                if self.frm == unit.split(",")[0] and self.to == unit.split(",")[1]:
                    return self.value/value
                elif self.to == unit.split(",")[0] and self.frm == unit.split(",")[1]:
                    return self.value*value
