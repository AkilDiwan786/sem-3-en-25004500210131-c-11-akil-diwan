class Student:
    def __init__(self):
        self.__marks = 80

    def show(self):
        print("Marks:", self.__marks)

s = Student()
s.show()