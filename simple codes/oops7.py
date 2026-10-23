class Student:
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.avg():.2f}")
# Example usage
name = input("Enter student name: ")
n = int(input("Enter the no of the sunjects: "))
marks = list(int(input(f"Enter marks for subject {i+1}: ")) for i in range(n))
student = Student(name, marks)
student.display()
