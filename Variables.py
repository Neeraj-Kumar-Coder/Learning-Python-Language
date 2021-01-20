var1 = "This is a string"  # Allocates the input to the desired type
var2 = 34
var3 = 4.636
print(var1)
print(var2)
print(var3)
print(type(var1))  # Prints the allocated type of the variable
print(type(var2))
print(type(var3))

# Arithmetics
var4 = " A lol string"
print(var2 + var3)
print(var1 + var4)
print(var2 - var3)

# Typecasting
var5 = "34"
var6 = "11"
print(var5 + var6)
print(int(var5) + int(var6))  # Typecasting is performed

# Loop equivalents
print(10 * "The string\n")
print(10 * int(var5) + int(var6))

# Typecasted to string to print 10 times
print(10 * str(int(var5) + int(var6)))

# Taking input from the user
print("Enter a number ")
var = input()
print("The number you entered is =", var)
print("Added 10 to your input = ", int(var) + 10)

# Simple addition calculator
print("Enter the first number = ", end="")
number1 = input()
print("Enter the second number = ", end="")
number2 = input()
print("The sum is =", int(number1) + int(number2))