#Create Student class with attributes and methods by oops
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
# Create an instance of the Student class
student1 = Student("Alice", 20, "A")
# Call the display_info method to show the student's information
student1.display_info()
# to take input from user
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grade = input("Enter student's grade: ")
# Create another instance of the Student class using user input
student2 = Student(name, age, grade)
# Call the display_info method to show the second student's information
student2.display_info()
