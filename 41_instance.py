class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

s = Student("Amit")
print(s.name)
print(s.college)