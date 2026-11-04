#Evalute a python that prompts the user to entera number and check the no is positive or zero ,otherwise give an exception value error
def check_positive_number():
    try:
        number = float(input("Please enter a number: "))
        if number >0:
            print("The number is positive.")
        elif number == 0:
            print("The number is zero.")
        else:
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter a positive number or zero.")
check_positive_number()