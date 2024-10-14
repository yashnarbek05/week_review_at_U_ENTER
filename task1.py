
deposite = 0
while True:
    price = 0
    amount = 0
    if input("is the bottle one liter or less? (yes or no): ") == "yes":
        price = 0.10
    else:
        price = 0.25

    amount = int(input("enter amount of bottles: "))
    deposite += amount * price
    print("your deposite:", deposite)

    if input("do you have other bottles: ") == "no":
        break



