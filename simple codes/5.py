#to take a binary integer and convert it to a decimal , octal,hexadecimal
def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[-(i+1)]) * (2 ** i)
    return decimal
def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal
def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = ''
    hex_digits = '0123456789ABCDEF'
    while decimal > 0:
        hexadecimal = hex_digits[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal
binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
octal_output = binary_to_octal(binary_input)
hexadecimal_output = binary_to_hexadecimal(binary_input)
print(f"Decimal: {decimal_output}")
print(f"Octal: {octal_output}")
print(f"Hexadecimal: {hexadecimal_output}")
# by using built in functions
binary_input = input("Enter a binary number: ")
decimal_output = int(binary_input, 2)
octal_output = oct(decimal_output)[2:]
hexadecimal_output = hex(decimal_output)[2:].upper()
print(f"Decimal: {decimal_output}")
print(f"Octal: {octal_output}")
print(f"Hexadecimal: {hexadecimal_output}")