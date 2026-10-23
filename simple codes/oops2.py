#Add grade calculation method by oops
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        average = sum(self.marks) / len(self.marks)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
# Example usage
student1 = Student("Alice", [85, 92, 78])
grade = student1.calculate_grade()
print(f"{student1.name}'s grade: {grade}")