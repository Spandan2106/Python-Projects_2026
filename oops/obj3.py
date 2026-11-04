#python class that has class Numbers with a method to find the maximum and minimum number from a list of numbers without using built-in functions.
class Numbers:
    def __init__(self, num_list):
        self.num_list = num_list

    def find_max_min(self):
        if not self.num_list:
            return None, None  # Return None if the list is empty

        max_num = self.num_list[0]
        min_num = self.num_list[0]

        for num in self.num_list:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num

        return max_num, min_num
# Example usage
n = int(input("Enter the number of elements in the list: "))
num_list = list(int (input(f"Enter element {i + 1}: ")) for i in range(n))
numbers = Numbers(num_list)
max_num, min_num = numbers.find_max_min()
print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
