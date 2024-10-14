from logging import exception

year = "1"

while year:
    try:
        year = int(input("Enter year: "))
    except:
        print("Enter number")
        continue

    if year % 400 == 0:
        print(f"{year} is leap year")
    elif year % 100 == 0:
        print(f"{year} is not leap year")
    elif year % 4 == 0:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")

    if input("Do you continue? yes or no: ") == "no":
        break
