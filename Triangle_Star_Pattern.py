def starPattern(size):
    linenum = 1
    while(linenum != size+1):
        temp1 = size - linenum
        temp2 = linenum
        while(temp1):
            print(" ", end="")
            temp1 -= 1
        while(temp2):
            print("*", end=" ")
            temp2 -= 1
        print("\n", end="")
        linenum += 1

height = input("Enter the height of the star pattern you want to get: ")
starPattern(int(height))