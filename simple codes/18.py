#Develop a Python program to find the volume of a Cuboid
def cauculate_volume(length, width, height):
    volume = length * width * height
    return volume
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
volume = cauculate_volume(length, width, height)
print("The volume of the cuboid is:", volume)