
text = "hello"
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("String:", text)
print("Character Frequency:", frequency)