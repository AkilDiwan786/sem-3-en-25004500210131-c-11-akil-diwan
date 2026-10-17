f = open("demo.txt", "r")
lines = f.readlines()
print("Total lines:", len(lines))
f.close()