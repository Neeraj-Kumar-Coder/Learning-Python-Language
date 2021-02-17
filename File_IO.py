fptr = open("Sample.txt", "r")
# content = fptr.read()
# print(content)

# for line in fptr: # To read line by line
#     print(line, end="")
lists = fptr.readlines() # Returns a list containing the lines
print(lists, end="")
fptr.close()
