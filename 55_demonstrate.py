
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        self.marks = marks

    def display(self):
        super().display()
        print("Course:", self.course)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")


s = Student("Rahul", 20, "Python", 80)

s.display()
s.result()