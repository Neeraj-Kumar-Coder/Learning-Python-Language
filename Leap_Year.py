# LEAP YEAR FINDER
year = int(input("Enter the year: "))
if not year % 400 or not year % 4 and year % 100:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
