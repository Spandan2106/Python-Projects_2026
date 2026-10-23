#Distinguish Absolute value, Square root and Cube of a number using user defined function in python.
def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num
def square_root(num):
    if num < 0:
        return "Square root is not defined for negative numbers."
    else:
        return num ** 0.5
def cube(num):
    return num ** 3
number = float(input("Enter a number: "))
print("Absolute value:", absolute_value(number))
print("Square root:", square_root(number))
print("Cube:", cube(number))
