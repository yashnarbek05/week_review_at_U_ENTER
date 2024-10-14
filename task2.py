
tax = 0
tip = 0

cost = 0

cost = float(input("Enter cost of meal ordered: "))

tax = 12 * cost / 100
tip = 18 * cost / 100

print("tip:", tip)
print("tax:", tax)
print("Grand total:", tax + tip + cost)
