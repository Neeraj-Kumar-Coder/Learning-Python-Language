mystr = "Neeraj Kumar is Legend"
print(len(mystr))
print(mystr)
print(mystr[3])
print(mystr[0:6])
print(mystr[0:22])
# Advance slicing
print(mystr[0:6:2]) # It will print the string character having index multiple of 2 (the last character)
print(mystr[1:6:2])

# Negative indices
str1="Monty Python"
str2="monty57Python"
longstr="Neeraj is a very good boy and a Legend also"
print(str1[0:5])
print(str1[-6:])
print(str1[::-1]) # It will reverse the string

# Some functions
print(str2.isalnum()) # This will tell whether the string is apha numeric or not
print(str1.isalnum()) # This will tell whether the string is apha numeric or not
print(str1.isalpha()) # This will tell whether the string is aphabetic or not
print(str2.isalpha()) # This will tell whether the string is aphabetic or not
print(str2.endswith("thon")) # This will check whether the string ends with the provided string or not
print(str2.count("o")) # This will count the occurence of the input string in the source string
print(str2.count("on")) # This will count the occurence of the input string in the source string
print(str2.capitalize()) # This will capitalize the first character
print(longstr.find("a")) # This will return the position of the first occurence of the provided string in the main string
print(str2.lower()) # This will converts the entire string to lower case
print(str2.upper()) # This will converts the entire string to upper case
print(longstr.replace("a","Z")) # This will replace all the occurence of "a" with "Z"