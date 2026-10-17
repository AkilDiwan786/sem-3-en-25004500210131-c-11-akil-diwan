try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = a + b
    elif choice == 2:
        result = a - b
    elif choice == 3:
        result = a * b
    elif choice == 4:
        result = a / b
    else:
        raise ValueError("Invalid choice")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError as e:
    print("Error:", e)

else:
    print("Result:", result)

finally:
    print("Calculator program ended.")