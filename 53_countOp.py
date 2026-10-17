# Program to count lines, words and characters in a file

try:
    with open("data.txt", "r") as f:
        data = f.read()

    lines = data.splitlines()
    words = data.split()
    characters = len(data)

    print("File Content:")
    print(data)

    print("Total Lines:", len(lines))
    print("Total Words:", len(words))
    print("Total Characters:", characters)

except FileNotFoundError:
    print("Error: File not found.")
