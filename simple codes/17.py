n = int(input("Enter the no of steps: "))
a = 65
for i in range(n):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(0,i+1):
        print(chr(a+k),end=" ")
    a = a + 1
    print()
    