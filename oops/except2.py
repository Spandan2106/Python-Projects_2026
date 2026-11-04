#Create a python program that infinitely print natural numbers .Raise the Stop iteration exception after displaying first 20 natural numbersto exit the loop.
def generate_natural_numbers():
    num = 1
    while num <= 20:
        yield num
        num += 1
    return "Reached the limit of 20 natural numbers."

numbers_generator = generate_natural_numbers()

try:
    while True:
        print(next(numbers_generator), end=' ')
except StopIteration as e:
    print(f"\nLoop stopped: {e.value}")