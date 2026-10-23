#Make use of Python program that creates a Dictionary of a Radius (that taken by user) andits Circumference for a Circle.
import math
def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference
radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
circle_info = {"Radius": radius,
"Circumference": circumference}
print(circle_info)
