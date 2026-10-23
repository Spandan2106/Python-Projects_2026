# Develop a Python program that calculates Fibonacci of N numbers using a Dictionary
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
N = int(input("Enter the number of Fibonacci numbers to calculate: "))
fib_sequence = [fibonacci(i) for i in range(N)]
print(f"Fibonacci sequence up to {N} numbers: {fib_sequence}")
