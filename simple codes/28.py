#Evaluate a Python program that promptsthe user to enter a number and check the number is Positive or zero, otherwise raise an exception Value Error.
def check_number(num):
    if num > 0:
        print("The number is Positive.")
    elif num == 0:
        print("The number is Zero.")
    else:
        raise ValueError("The number is Negative. Please enter a positive number or zero.")
try:
    user_input = float(input("Enter a number: "))
    check_number(user_input)
except ValueError as e:
    print(e)
    
