#Determine a Python program that randomly generates a number. Raise a user-defined exception if the number is below 0.1.
import random
def check_random_number():
    num = random.random()
    print(f"Generated number: {num}")
    if num < 0.1:
        raise ValueError("The generated number is below 0.1. Please try again.")
try:
    check_random_number()
except ValueError as e:
    print(e)
    