class Num:
    def __init__ (self,num):
        self.num = num
    def minmax(self):
        if not self.num:
            return None,None
        min_num = self.num[0]
        max_num = self.num[0]
        for n in self.num:
            if n < min_num:
                min_num = n
            if n > max_num:
                max_num = n
        return min_num, max_num
n = int(input("Enter the number of elements: "))
numbers = list(int(input("enter :")) for i in range(n))
num_obj = Num(numbers)
min_num, max_num = num_obj.minmax()
print("Minimum number:", min_num)
print("Maximum number:", max_num)