def leftStarPrint(size):
    """This function will print the star pattern with spaces on left"""  # This is a docstring
    linenum = 1
    while(linenum != size+1):
        temp1 = size - linenum
        temp2 = linenum
        while(temp1):
            print(" ", end="")
            temp1 -= 1
        while(temp2):
            print("*", end="")
            temp2 -= 1
        print("\n", end="")
        linenum += 1


def rightStarPrint(size):
    """This function will print the star pattern with spaces on right"""  # This is a docstring
    linenum = 1
    while(linenum != size+1):
        temp = linenum
        while(temp):
            print("*", end="")
            temp -= 1
        print("\n", end="")
        linenum += 1


# print(leftStarPrint.__doc__)  # Used to print docstrings
# print(rightStarPrint.__doc__)  # Used to print docstrings

height = input("Enter the size of star pattern you want: ")
leftStarPrint(int(height))
rightStarPrint(int(height))