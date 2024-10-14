import re

str = input("Enter license plate: ")

if (re.search("[A-Z][A-Z][A-Z][0-9][0-9][0-9]",str)
        or re.search("[0-9][0-9][0-9][0-9][A-Z][A-Z][A-Z]",str)):
    print(f"{str} is valid license")
else:
    print(f"{str} is not valid license")