# reverse string without using built in functions
def reverse_string(s):
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string
# example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)