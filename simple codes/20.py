#Develop a Python program that accept a String from User and Re-display the same after removing Vowels from it (use user defined function).
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result
# Get input from the user
user_input = input("Enter a string: ")
# Remove vowels and display the result
output = remove_vowels(user_input)
print("String after removing vowels:", output)
#Make use of Python program to reverse a string
def reverse(s):
    print("Reversed string is: ", end="")
    for i in range(len(s)-1, -1, -1):
        print(s[i], end="")
# Get input from the user
S = input("Enter a string to reverse: ")
reverse(S)
#Utilize Python programming concept that accepts a string from user. It will create a new string by shifting one position to left
def shift_left(input_string):
    if len(input_string) == 0:
        return input_string
    return input_string[1:] + input_string[0]
# Get input from the user
user_input = input("\nEnter a string to shift left: ")
# Shift the string and display the result
shifted_string = shift_left(user_input)
print("String after shifting left:", shifted_string)
#Develop a program that asks the user to input his name and print its initials. Assuming that the user always types first name, middle name and last name and does not include any unnecessary spaces
def get_initials(name):
    parts = name.split()
    initials = ""
    for part in parts:
        initials += part[0].upper() + "."
    return initials
# Get input from the user
user_name = input("\nEnter your full name (first name, middle name, last name): ")
# Get initials and display the result
initials = get_initials(user_name)
print("Your initials are:", initials)
