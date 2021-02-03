#User interface
from formulas import Geometry

def main():
    running = True
    while running:
        cal = (input("Enter C for Cirle.... Enter A for Triangle..... Enter S for Square.... Enter Q to Quit\\\nEnter T  for Trapezium.... Enter P for Parallelogram.... \nEnter: " )).upper()
        if cal == "Q":
            running = False
        elif cal == "C":
            try:
                r = float(input("Enter Radius: "))
            except:
                print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                continue
            circle = Geometry.Circle(r)
            geometry = (input("Enter A for Area.... Enter C for Circumference......  Enter D for Diameter \n Enter: ")).upper()
            if geometry == "A":
                print("############\n",circle.area(),"\n###########")
            elif geometry == "C":
                print("############\n",circle.circumference(),"\n###########")
            elif geometry == "D":
                print("############\n",circle.diameter(),"\n###########")
            else:
                print("############\ninvalid entry\n###########")

        elif cal == "A":
            geometry = (input("Enter A for Area.... Enter P for Perimeter\n Enter: ")).upper()
            if geometry == "A":
                try:
                    base = float(input("Enter Base: "))
                    height = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                triangle = Geometry.Triangle(height, base)
                print("############\n",triangle.area(),"\n###########")
            elif geometry == "P":
                try:
                    base = float(input("Enter Base: "))
                    height = float(input("Enter Side A: "))
                    side = float(input("Enter Side B: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                triangle = Geometry.Triangle(height, base, side)
                print("############\n",triangle.perimeter(),"\n###########")
            else:
                print("############\ninvalid entry\n###########")

        elif cal == "S":
            try:
                lenght = float(input("Enter Lenght: "))
                width = float(input("Enter Width: "))
            except:
                print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                continue
            square = Geometry.Square(lenght, width)
            geometry = (input("Enter A for Area.... Enter P for Perimeter\n Enter: ")).upper()
            if geometry == "A":
                print("############\n",square.perimeter(),"\n###########")
            elif geometry == "P":
                print("############\n",square.perimeter(),"\n###########")

            else:
                print("############\ninvalid entry\n###########")

        elif cal == "T":
            geometry = (input("Enter A for Area.... Enter P for Perimeter\n Enter: ")).upper()
            if geometry == "A":
                try:
                    baseA = float(input("Enter Base A: "))
                    baseB = float(input("Enter Base B: "))
                    height = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                trapezium = Geometry.Trapezium(baseA, baseB, height)
                print("############\n",trapezium.area(),"\n###########")
            elif geometry == "P":
                try:
                    baseA = float(input("Enter Base A: "))
                    baseB = float(input("Enter Base B: "))
                    sideA = float(input("Enter Side A: "))
                    sideB = float(input("Enter Side B: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                trapezium = Geometry.Trapezium(baseA, baseB, sideA, sideB)
                print("############\n",trapezium.perimeter(),"\n###########")
            else:
                print("############\ninvalid entry\n###########")

        elif cal == "P":
            geometry = (input("Enter A for Area.... Enter P for Perimeter\n Enter: ")).upper()
            if geometry == "A":
                try:
                    base = float(input("Enter Base: "))
                    height = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                parallelogram = Geometry.Parallelogram(base, height)
                print("############\n",parallelogram.area(),"\n###########")
            elif geometry == "P":
                try:
                    base = float(input("Enter Base: "))
                    side = float(input("Enter Side: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                parallelogram = Geometry.Parallelogram(base, height)
                print("############\n",parallelogram.perimeter(),"\n###########")
            else:
                print("############\ninvalid entry\n###########")

        else:
            print("############\ninvalid entry\n###########")
if __name__ == "__main__":
    main()
