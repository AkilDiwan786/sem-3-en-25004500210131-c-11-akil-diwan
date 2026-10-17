numbers = [20, 45, 10, 35, 50]

print("Original List =", numbers)

# Append
n = int(input("Enter number to add: "))
numbers.append(n)

print("After Append =", numbers)

# Maximum
print("Maximum =", max(numbers))

# Minimum
print("Minimum =", min(numbers))

# Average
average = sum(numbers) / len(numbers)
print("Average =", average)

# Sort
numbers.sort()
print("Sorted List =", numbers)

# Find
search = int(input("Enter number to find: "))

if search in numbers:
    print("Number Found")
else:
    print("Number Not Found")