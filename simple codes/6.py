# to print floyds triangle
n = int(input("Enter the number of rows: "))
num = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
    print()
# to prnit floyds triangle in reverse order
n = int(input("Enter the number of rows: "))
num = n * (n + 1) // 2
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num -= 1
    print()
# to print A to Z in floyds triangle
n = int(input("Enter the number of rows: "))
num = 65
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(num), end=' ')
        num += 1
    print()  