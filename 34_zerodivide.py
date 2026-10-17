try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Cannot divide by zero")