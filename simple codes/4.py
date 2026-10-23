# to take float as string then print the int and decimal part separately
num = input("Enter a float number: ")
c = 0
for i in num:
    if i == '.':
        break
    c += 1
l = num[0:c]
m = num[c+1:]
print("Integer part: ", l)
print("Decimal part: ", m)