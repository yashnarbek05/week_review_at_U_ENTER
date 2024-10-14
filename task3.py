import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

disc = b ** 2 + 4 * a * c

if disc > 0:
    root1 = (-1 * b + math.sqrt(disc)) / (2 * a)
    root2 = (-1 * b - math.sqrt(disc)) / (2 * a)
    print(f"""root1 is {root1:.2f}, root2 is {root2:.2f}
    if root2 is 0, desc is 0""")
elif disc < 0:
    print("There is not any root bcs of desc")
else:
    root1 = (-1 * b) / (2 * a)
    print(f"root1 is {root1:.2f}")

