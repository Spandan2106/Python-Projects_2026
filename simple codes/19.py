#Encrypt the given message by adding a key value to everycharacter (Caesar Cipher) using python language Input: H E L L O +3 Output: K H O O R
def caesar_cipher(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            shift = key % 26  # Ensure the key is within the range of the alphabet
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-alphabet characters remain unchanged
    return encrypted_message
# Example usage
message = "HELLO"
key = 3
encrypted_message = caesar_cipher(message, key)
print(encrypted_message)  # Output: KHOOR
# user input
message = input("Enter the message to encrypt: ")
key = int(input("Enter the key value: "))
encrypted_message = caesar_cipher(message, key)
print("Encrypted message:", encrypted_message)
