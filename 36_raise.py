age = 15

try:
    if age < 18:
        raise ValueError("Not eligible")
    print("Eligible")
except ValueError as e:
    print(e)