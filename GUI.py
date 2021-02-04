#User interface
from formulas import Geometry, Conversion

def main():
    running = True
    while running:
        mode = (input("Enter GE for Geometry.... Enter CO for Conversion......\
                    \nEnter: " )).upper()

        if mode == "Q":
            running = False
        elif mode == "GE":
            cal = (input("Enter CI for Cirle.... Enter TI for Triangle..... Enter SQ for Square.... Enter Q to Quit\
                        \nEnter TA  for Trapezium.... Enter PA for Parallelogram.... Enter CU for Cube...\
                        \nEnter SP for Sphere.... Enter CO for Cone.... Enter CY for Cylinder....\
                        \nEnter: " )).upper()
            if cal == "CI":
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

            elif cal == "TI":
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

            elif cal == "SQ":
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

            elif cal == "TA":
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

            elif cal == "PA":
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

            elif cal == "CU":
                try:
                    lenght = float(input("Enter Lenght: "))
                    width = float(input("Enter Width: "))
                    height = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                cube = Geometry.Cube(lenght, width, height)
                geometry = (input("Enter A for Surface Area.... Enter V for Volume\n Enter: ")).upper()
                if geometry == "V":
                    print("############\n",cube.volume(),"\n###########")
                elif geometry == "A":
                    print("############\n",cube.surface_area(),"\n###########")

                else:
                    print("############\ninvalid entry\n###########")

            elif cal == "SP":
                try:
                    radius = float(input("Enter Radius: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                sphere = Geometry.Sphere(radius)
                geometry = (input("Enter A for Surface Area.... Enter V for Volume\n Enter: ")).upper()
                if geometry == "V":
                    print("############\n",sphere.volume(),"\n###########")
                elif geometry == "A":
                    print("############\n",sphere.surface_area(),"\n###########")

                else:
                    print("############\ninvalid entry\n###########")

            elif cal == "CO":
                try:
                    radius = float(input("Enter Radius: "))
                    height = radius = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                cone = Geometry.Cone(radius, height)
                geometry = (input("Enter A for Surface Area.... Enter V for Volume\n Enter: ")).upper()
                if geometry == "V":
                    print("############\n",cone.volume(),"\n###########")
                elif geometry == "A":
                    print("############\n",cone.surface_area(),"\n###########")

                else:
                    print("############\ninvalid entry\n###########")

            elif cal == "CY":
                try:
                    radius = float(input("Enter Radius: "))
                    height = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                cylinder = Geometry.Cylinder(radius, height)
                geometry = (input("Enter A for Surface Area.... Enter V for Volume\n Enter: ")).upper()
                if geometry == "V":
                    print("############\n",cylinder.volume(),"\n###########")
                elif geometry == "A":
                    print("############\n",cylinder.surface_area(),"\n###########")

                else:
                    print("############\ninvalid entry\n###########")

            else:
                print("############\ninvalid entry\n###########")
        elif mode == "CO":
            cal = (input("Enter LE for lenght... Enter VO for Volume.....\nEnter: " )).upper()
            try:
                value = float(input("Enter Value: "))
                frm = (input("Enter From SI Unit: ")).lower()
                to = (input("Enter To SI Unit: ")).lower()
            except:
                print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                continue
            if cal == "LE":
                conversion = Conversion.Lenght(value, frm, to)
                print("############\n",conversion.converter(),"\n###########")
            elif cal == "VO":
                conversion = Conversion.Volume(value, frm, to)
                print("############\n",conversion.converter(),"\n###########")
            else:
                print("############\ninvalid entry\n###########")
        else:
            print("############\ninvalid entry\n###########")
if __name__ == "__main__":
    main()
