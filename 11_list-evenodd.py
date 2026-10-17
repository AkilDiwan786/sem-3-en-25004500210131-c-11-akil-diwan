numbers = [10, 15, 22, 7, 30, 41]

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)