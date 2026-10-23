#. Determine a Python program which w i l l throw an exception zero DivisionError in a division operation when the denominator is zero.
n = int(input("Enter the numerator: "))
d = int(input("Enter the denominator: "))
try:
    result = n / d
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    