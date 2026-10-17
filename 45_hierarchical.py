class Parent:
    def show(self):
        print("Parent class")

class A(Parent):
    pass

class B(Parent):
    pass

A().show()
B().show()