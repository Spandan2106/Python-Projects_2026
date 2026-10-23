PI = 3.14159
class Circle:
    PI = 3.14
    def __init__ (self,r):
        self.r = r
    def circum(self):
        return 2 * PI * (self.r)
    def area(self):
        return PI * (self.r)**2
r = float(input("Enter the radius : "))
cir = Circle(r)
print("The circumference of the circle is : ", cir.circum())
print("The area of the circle is : ", cir.area())