#Determine a Python program that has a class Numbers with values stored in a list. Write a method to find the largest value by oops
class Numbers:
    def __init__(self, values):
        self.values = values
    def find_largest(self):
        if not self.values:
            return None
        largest = self.values[0]
        for num in self.values:
            if num > largest:
                largest = num
        return largest
# Example usage
numbers = Numbers([3, 5, 7, 2, 8])
largest_value = numbers.find_largest()
print("The largest value is:", largest_value)
