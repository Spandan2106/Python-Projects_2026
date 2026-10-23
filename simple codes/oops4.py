#Demonstrate inheritance using Person and Employee by oops
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def __init__(self,name,age,empid):
        super().__init__(name,age)
        self.empid=empid
    def display(self):
        super().display()
        print("Employee ID:",self.empid)
#Create an Employee object
emp=Employee("Alice",30,"E123")
emp.display()
