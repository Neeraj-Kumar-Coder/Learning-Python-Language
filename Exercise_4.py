height = int(input("Enter the number of rows you want in your star pattern: "))
boolVar = int(input("Enter any number for True and 0 for False: "))
if boolVar == True:
    linenum = 1
    while(linenum != height+1):
        temp = linenum
        while(temp):
            print("*", end="")
            temp -= 1
        print()
        linenum += 1
else:
    linenum = height
    while(linenum):
        temp = linenum
        while(temp):
            print("*", end="")
            temp -= 1
        print()
        linenum -= 1