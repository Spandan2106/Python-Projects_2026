# to chkeck whether the given number is prime or not
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# to get the prime numbers in a given range
def prime_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if isprime(num):
            primes.append(num)
    return primes
# to print tribonacci series up to n terms
def tribonacci(n):
    a, b, c = 0, 1, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b, c = b, c, a + b + c
    return series
# same by recursion
def tribonacci_recursive(n, a=0, b=1, c=1, series=None):
    if series is None:
        series = []
    if n > 0:
        series.append(a)
        return tribonacci_recursive(n - 1, b, c, a + b + c, series)
    return series
# to check whether the given number is armstrong or not
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n
# to print armstrong numbers in a given range
def armstrong_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
# input from user
n = int(input("Enter a number to check if it's prime: "))
print(f"{n} is {'a prime number' if isprime(n) else 'not a prime number'}.")

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end}: {prime_in_range(start, end)}")
n_terms = int(input("Enter the number of terms for Tribonacci series: "))
print(f"Tribonacci series up to {n_terms} terms: {tribonacci(n_terms)}")
print(f"Tribonacci series (recursive) up to {n_terms} terms: {tribonacci_recursive(n_terms)}")
start1 = int(input("Enter the start of the range for Armstrong numbers: "))
end1 = int(input("Enter the end of the range for Armstrong numbers: "))
print(f"Armstrong numbers between {start} and {end}: {armstrong_in_range(start1, end1)}")
p = int(input("Enter a number to check if it's an Armstrong number: "))
print(f"{p} is {'an Armstrong number' if is_armstrong(p) else 'not an Armstrong number'}.")
