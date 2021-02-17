# LEAP YEAR FINDER
year = int(input("Enter the year: "))
if not year % 400 or not year % 4 and year % 100:
    print("It's a leap year")
else:
    print("It's not a leap year")
