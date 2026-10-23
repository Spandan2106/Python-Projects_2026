import math
def absolute(n):
    if n<0:
        print(f"{n} is negative,absolute value is {abs(n)}")
    else:
        print(f"{n} is positive,absolute value is {abs(n)}")
def check_squre(n):
    if n<0:
        print(f"{n} is negative,so it can't be a perfect square")
    root = int(math.sqrt(n))
    
    if root*root == n:
        print(f"{n} is a perfect square")
    else:
        print(f"{n} is not a perfect square")
def check_cube(n):
    if n<0:
        print(f"{n} is negative,so it can't be a perfect cube")
    root = int(round(n ** (1/3)))
    
    if root**3 == n:
        print(f"{n} is a perfect cube")
    else:
        print(f"{n} is not a perfect cube")
n = int(input("Enter a number: "))
absolute(n)
check_squre(n)
check_cube(n)

        