# Revision string
"""
   This
   is
   multi-line
   comment
"""
""" print("Hello, World")  # This is a single comment
print("This should not come in a new line.", end="")
print(" Auto", "Space", end="")
print("...End...")
var1 = "This variable is a string"
var2 = 10
var3 = 'a'
print(var1, var2, var3)
print(type(var1), type(var2), type(var3))
print(5*"Programming is awesome\n")
# Calculator code
num_1 = input("Enter the value of number 1 = ")
num_2 = input("Enter the value of number 2 = ")
operation = input("Enter the operation you want to perform = ")
try:
    print(int(num_1), operation, int(num_2), "= ", end="")
    if operation == "+":
        print(int(num_1)+int(num_2))
    elif operation == "-":
        print(int(num_1)-int(num_2))
    elif operation == "*":
        print(int(num_1)*int(num_2))
    elif operation == "/":
        print(int(num_1)/int(num_2))
    elif operation == "//":
        print(int(num_1)//int(num_2))
    elif operation == "%":
        print(int(num_1) % int(num_2))
    else:
        print("Unrecognized Operation\nBhai enter a valid input!!")
except Exception as Reason:
    print(Reason) """

# More recap from here
""" Advanced Slicing :: string[a1:a2:n], prints the string from a1 to (a2 - 1) by jumping n characters
if, a1 is empty : default is 0
if, a2 is empty : default is full length
if, n is empty : default is 1 """
""" sample_string = "This is a sample string"
print(len(sample_string))  # Prints the length of the string
print(sample_string)  # To print full string
print(sample_string[5])  # To print a specific character in the position 5
print(sample_string[0:6])  # To print the string from 0 to 5
# To print the string from 4 to 16 by jumping 2 characters
print(sample_string[4:17:2])
print(sample_string[::-1])  # It will reverse and print the whole string
# It will print the character at position -2 (the position -1 is the last character)
print(sample_string[-2])

string = "ThisIsAlphaNumeric007"
string1 = "ThisIsAphabetic"
string2 = "all letters are small"
print(string.isalnum())  # Checks if the string is alpha numeric
print(string1.isalpha())  # Checks if the string is alphabetic
# Checks if the string ends with the specified string
print(string.endswith("c007"))
# Returns the number of occurences of the specified string
print(string.count("p"))
# This will return the capitalized first character of the string (it doesn't alter the original string)
print(string2.capitalize())
# It will return the position of occurence of the specified string (if found), else return -1
print(string.find("Is"))
print(string.lower())
print(string.upper())
print(string.lower().replace("is", "CHANGED"))
print(string.replace("is", "CHANGED").lower()) """

# List
""" this_is_a_list = ["item1", "item2", "item3", 50, "item5", 100]
print(this_is_a_list)
print(this_is_a_list[3])
print(type(this_is_a_list))
print(type(this_is_a_list[3]))

number_list = [52, 69, 15, 74, 93, 62, 54, 10, 20, 98, 506, 62, 3254, 55, 2, 3, 554]
print("The number of elements in the list is =",len(this_is_a_list),"\nNumber of elements in number_list =",len(number_list))
print(number_list)
number_list.sort()
print(number_list)
number_list.reverse()
print(number_list)
print(number_list[0:3])
print(number_list[::2])
print(number_list[::-1])
print(max(number_list))
print(min(number_list))
number_list.append(13.5)
print(number_list)
number_list.insert(1,9)
number_list.remove(52)
number_list.pop(1)
print(number_list) """

# Tuple
""" this_is_a_tuple = (10, 20, "string")
print(type(this_is_a_tuple))
print(this_is_a_tuple)
print(this_is_a_tuple[1]) """

# Dictionary
""" favorite_food = {"Bittu": {"Day":"Doodh roti","Night":"Daal bhaat"}, "Neha": "Pizza", "Mummy": "Jelabi", "Papa": "Daal bhaat chokha",'a':'b',5_2:25}
print(favorite_food)
print(favorite_food.keys())
print(favorite_food.values())
name = input("Enter the name of the person: ")
try:
    print("The favourite food of", name.capitalize(), "is", favorite_food[name.capitalize()])
except:
    print("The specified person is not in the list")
print(favorite_food['a'])
print(type(favorite_food[5_2]))
print(favorite_food["Bittu"]["Night"])
favorite_food.update({"Bittu":"Chola bhatura","Ram":"Maggie"})
print(favorite_food)
print(favorite_food.keys())
print(favorite_food.values())
print(favorite_food.items()) """

# Sets
""" this_is_a_set_from_list = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a_set = {1, 2, 3, 4, 5}
print(this_is_a_set_from_list)
print(len(this_is_a_set_from_list)) """

# Control statements
""" a_set = {1, 2, 3, 4, 5, "lol"}
print(type(a_set))
print(a_set)
if "lol" in a_set:
    print("Yes")
else:
    print("No")
print(5 in a_set) """