#evalute a python program,that has an abstract class Polygon .Derive two subclasses Rectangle and Triangle from the Polygon class and write methods to get details of their dimentions and hence calculate the area of the rectangle and triangle.
class Polygon:
    def __init__(self,len):
        self.len = len
    def area(self):
        pass
class Rectangle(Polygon):
    def __init__(self,len,breadth):
        Polygon.__init__(self,len)
        self.breadth = breadth
    def area(self):
        return self.len * self.breadth
class Triangle(Polygon):
    def __init__(self,base,height):
        Polygon.__init__(self,base)
        self.height = height
    def area(self):
        return 0.5 * self.len * self.height
# Example usage:
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
rectangle = Rectangle(l, b)
print("Area of Rectangle:", rectangle.area())
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle = Triangle(base, height)
print("Area of Triangle:", triangle.area())
