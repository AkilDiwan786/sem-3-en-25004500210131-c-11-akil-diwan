

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)

    def calculate_result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")

roll = int(input("Enter roll number: "))
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

s = Student(roll, name, marks)

s.display()
s.calculate_result()