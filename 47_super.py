class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("Child class")

Child().show()