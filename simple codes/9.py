# to remove duplicate from a string
def remove_duplicate(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result
s = "hello world"
print(remove_duplicate(s))
# to check if a string is a palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
s = "A man a plan a canal Panama"
print(is_palindrome(s))
#replace all space with hyphen without using built in function
def replace_space(s):
    result = ""
    for char in s:
        if char == " ":
            result += "-"
        else:
            result += char
    return result
s = "hello world"
print(replace_space(s))
