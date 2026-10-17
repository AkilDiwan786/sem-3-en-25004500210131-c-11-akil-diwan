numbers = [10, 25, 7, 40, 15]

total = 0
maximum = numbers[0]

for n in numbers:
    total = total + n

    if n > maximum:
        maximum = n

print("Sum =", total)
print("Maximum =", maximum)