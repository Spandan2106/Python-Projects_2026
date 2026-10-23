# conut vowels,consonents ,dists and spaces in a string
def count_vowels_consonants_dist_spaces(string):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    digit = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == ' ':
            space_count += 1
        else:
            digit += 1
            
    return vowel_count, consonant_count, space_count , digit
# Example usage
s = input("Enter a string: ")
vowels, consonants, spaces , digits = count_vowels_consonants_dist_spaces(s)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Digits: {digits}")
