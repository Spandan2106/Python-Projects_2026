import Rectangle as rec
import Circle as cir
import Equilateral_Triangle as tri
import Regular_Pentagon as pen
class Main:
    def __init__(self,l,br,r,a,b):
        self.l = l
        self.br = br
        self.r = r
        self.a = a
        self.b = b
    def Rectangle(self):
        print()
        print(f"Area of Rectangle:{rec.area(self.l,self.br):.2f}")
        print(f"Perimeter of Rectangle: {rec.perimeter(self.l,self.br):.2f}")
    def Circle(self):
        print()
        print(f"Area of Circle: {cir.area(self.r):.2f}")
        print(f"Circumference of Circle: {cir.circumference(self.r):.2f}")
    def Equi_triangle(self):
        print()
        print(f"Area of Equilateral Triangle: {tri.area(self.a):.2f}")
        print(f"Perimeter of Equilateral Triangle: {tri.perimeter(self.a):.2f}")
    def Reg_Pentagon(self):
        print()
        print(f"Area of Regular Pentagon: {pen.area(self.b):.2f}")
        print(f"Perimeter of Regular Pentagon: {pen.perimeter(self.b):.2f}")
l = float(input("Enter length of Rectangle: "))
br = float(input("Enter breadth of Rectangle: "))
r = float(input("Enter radius of Circle: "))
a = float(input("Enter side of Equilateral Triangle: "))
b = float(input("Enter side of Regular Pentagon: "))
obj = Main(l,br,r,a,b)
obj.Rectangle()
obj.Circle()
obj.Equi_triangle()
obj.Reg_Pentagon()
