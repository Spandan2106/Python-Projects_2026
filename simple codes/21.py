#Make use of Python program to create a Dictionary of Odd numbers in the range of 1 to 10
odd_numbers = {num: num for num in range(1, 11) if num % 2 != 0}
print(odd_numbers)
#by using function
def create_odd_number_dict(start, end):
    return {num: num for num in range(start, end + 1) if num % 2 != 0}
odd_numbers_dict = create_odd_number_dict(1, 10)
print(odd_numbers_dict)