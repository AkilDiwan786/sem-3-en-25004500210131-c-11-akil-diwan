# Program to perform file operations

def write_data():
    with open("student.txt", "w") as f:
        f.write("Name: Rahul\n")
        f.write("Course: Python\n")
        f.write("Marks: 85\n")

    print("Data written successfully.")

def append_data():
    with open("student.txt", "a") as f:
        f.write("College: ABC College\n")

    print("Data appended successfully.")

def read_data():
    try:
        with open("student.txt", "r") as f:
            print("\nFile Content:")
            print(f.read())

    except FileNotFoundError:
        print("File not found.")

write_data()
append_data()
read_data()