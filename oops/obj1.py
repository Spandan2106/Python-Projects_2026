# python programs to create a class student with attributes name and marks of the suubjects and  make average marks of each student , and a method display to print the details.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def display(self):
        avg = self.average_marks()
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {avg:.2f}")
# Example usage
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
student = Student(name, marks)
student.display()

