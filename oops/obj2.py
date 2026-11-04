#python of class has a circle class,a class vatriable pi and a method to calculate area of circle and circumference of circle.
class Circle:
    pi = 3.14159  # class variable

    def __init__(self, radius):
        self.radius = radius  # instance variable

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * Circle.pi * self.radius
# Example usage
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print(f"Area of the circle: {circle.area():.2f}")
print(f"Circumference of the circle: {circle.circumference():.2f}")
