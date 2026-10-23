#sorting by using oops
class Sorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def bubble_sort(self):
        n = len(self.numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.numbers[j] > self.numbers[j+1]:
                    self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]

    def display(self):
        print("Sorted numbers:", self.numbers)
# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter(numbers)
sorter.bubble_sort()
sorter.display()
