# *********************************************** This is a single line comment ***********************************************
"""
This is a
multiline comment
"""


from random import shuffle


print("Hello, World to the revision of the python language!")
print("First part of the string", "Second part of the same string")

# *********************************************** Escape Sequences ***********************************************
print("Escape sequences:")
print("1. This is\ttab")
print('2. This is "Inverted commas"')
print("3. This is 'Single quote'")
print("4. This is wrong\b\b\b\b\bright")

# *********************************************** Variables ***********************************************
var1 = "neeraj kumar"
var2 = 23.98
var3 = 22
var4 = [12, 234, 55, "hello", 22.22]

print(type(var1), "value ", var1)
print(type(var2), "value ", var2)
print(type(var3), "value ", var3)
print(type(var4), "value ", var4)

# *********************************************** Typecasting ***********************************************
var5 = str(var2)
print(type(var5), "value ", var5)

# *********************************************** Loop equivalent ***********************************************
print(5 * "This will be printed 5 times\n")

# *********************************************** Taking input from the user ***********************************************
print("Enter the two values to be added")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(num1 + num2)

# *********************************************** String slicings ***********************************************
testString = "ThisIsATestStringThatIsToBeSlicedMultipleTimes"
print("Original String is:", testString, "[length = ", len(testString), end="]\n")
print(testString[0:3])
print(testString[0:10:2])
print(testString[-12:])
print(testString[-10::3])
print(testString[::-1])

# *********************************************** List in python ***********************************************
testList = ["item1", 124, [1, 2, 3], 22.2]
print(testList)
testList.reverse()
print(testList, "[length=", len(testList), end="]\n")

# *********************************************** Tuple a.k.a. immutable list ***********************************************
testTuple = (1, 23, 34, 45, 55.5, "hello")
print(type(testTuple), testTuple)

onlyOneElementTuple = (1,)
print(type(onlyOneElementTuple), onlyOneElementTuple)

# *********************************************** Swapping heorically with python ***********************************************
a = 12
b = 22
a, b = b, a
print(a, b)

# *********************************************** Dictionary in python ***********************************************
testDictionary = {
    "Name": "Neeraj",
    "Age": 22,
    "College": "Netaji Subhas University of Technology",
    "Year": 3,
    "Graduation Year": 2024,
    "extra": 99,
}

del testDictionary["extra"]
deepCopyOfDict = testDictionary.copy()
shallowCopyOfDict = testDictionary

shallowCopyOfDict["new"] = "addedByShallowCopy"
print("DeepCopy:\t", deepCopyOfDict)
print("Original:\t", testDictionary)
print("ShallowCopy:\t", shallowCopyOfDict)

print("All Keys:\t", testDictionary.keys())
print("All Values:\t", testDictionary.values())
print("All Items:\t", testDictionary.items())

# *********************************************** Sets in python ***********************************************
testSet = set()
print(type(testSet))
testSet.add(12)
testSet.add(11)
testSet.add(123)
testSet.add(123)
print(testSet)

testSet.remove(123)
print(testSet)
print("Length of the set:", len(testSet))

# *********************************************** Control Statements ***********************************************
age = 22
if age < 18:
    print("Sorry you cannot vote!")
elif age > 18:
    print("You are allowed to vote!")
else:
    print("You are under process...")

family = ["Papa", "Mummy", "Neha", "Bittu"]
# name = input("Enter your name: ")
# if name.capitalize() in family:
#     print("Yes! you are in the family")
# else:
#     print("Sorry! You are NOT in the list provided!")

# *********************************************** Loops ***********************************************
print("Members of the family are: ", end="")
for member in family:
    print(member, end=", ")
print("\b\b ")

# *********************************************** Iterating nested lists ***********************************************
nestedList = [["name", "bittu"], ["age", 20]]
for item in nestedList:
    print(item)
for key, value in nestedList:
    print(key, value)

# *********************************************** Iterating dict ***********************************************
for key, value in testDictionary.items():
    print(key, "=>", value)

# *********************************************** Shorhand if-else ***********************************************
number1 = 10
number2 = 7
print("number1 is greater than number2") if (number1 > number2) else print(
    "number2 is greater of equal to number1"
)

# *********************************************** Empty loops ***********************************************
for _ in range(10):
    pass

# *********************************************** Functions in python ***********************************************
dp = [-1] * 10000


def fibonacci(number):
    """This function will calculate the nth fibonaccin number"""
    if number == 0 or number == 1:
        return number
    if dp[number] != -1:
        return dp[number]
    dp[number] = fibonacci(number - 1) + fibonacci(number - 2)
    return dp[number]


print(fibonacci(10))

# *********************************************** Exception handing ***********************************************
integer1 = input("Enter the first number: ")
integer2 = input("Enter the second number: ")
try:
    print("The sum of the values is =", int(integer1) + int(integer2))
except Exception as err:
    print(err)

# *********************************************** 'else' after the for loop ***********************************************
for _ in range(10):
    print(_)
    # break
else:
    print("Loop exited normally")
