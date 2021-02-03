#User interface
from formulas import Circle, Triangle, Square

def main():
    running = True
    while running:
        cal = (input("Enter C for Cirle.... Enter T for Triangle..... Enter S for Square.... Enter Q to Quit\n Enter: " )).upper()
        if cal == "Q":
            running = False
        elif cal == "C":
            try:
                r = float(input("Enter Radius: "))
            except:
                print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                continue
            circle = Circle(r)
            geometry = (input("Enter A for Area.... Enter C for Circumference......  Enter D for Diameter \n Enter: ")).upper()
            if geometry == "A":
                print("############\n",circle.area(),"\n###########")
            elif geometry == "C":
                print("############\n",circle.circumference(),"\n###########")
            elif geometry == "D":
                print("############\n",circle.diameter(),"\n###########")
        elif cal == "T":
            geometry = (input("Enter A for Area.... Enter P for Perimeter\n Enter: ")).upper()
            if geometry == "A":
                try:
                    base = float(input("Enter Base: "))
                    height = float(input("Enter Height: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                triangle = Triangle(height, base)
                print("############\n",triangle.area(),"\n###########")
            elif geometry == "P":
                try:
                    base = float(input("Enter Base: "))
                    height = float(input("Enter Side A: "))
                    side = float(input("Enter Side B: "))
                except:
                    print("############\ninvalid Entry.... Insert Numbers Only\n###########")
                    continue
                triangle = Triangle(height, base, side)
                print("############\n",triangle.perimeter(),"\n###########")
        else:
            print("############\ninvalid entry\n###########")
if __name__ == "__main__":
    main()
