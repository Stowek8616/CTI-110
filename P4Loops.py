numCount = int(input("Enter a number of values to add: "))
total = 0
for i in range(numCount):
    num = float(input("Enter a number:"))
    total = num + total
print("Total: ", total)