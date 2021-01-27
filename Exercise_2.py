# Faulty Calculator
num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
operation = input("Enter the operation you want to perform : ")

wrongcalcs = {"99*33": "3417",
              "453/91": "4.73807563",
              "274+112": "236",
              "33*99": "3417",
              "112+274": "236"}  # Dictionary of wrong caclulations

if num1+operation+num2 in wrongcalcs:
    print(num1, operation, num2, "=", wrongcalcs[num1+operation+num2])
else:
    if operation == "+":
        print(num1, operation, num2, "=", int(num1)+int(num2))
    elif operation == "-":
        print(num1, operation, num2, "=", int(num1)-int(num2))
    elif operation == "*":
        print(num1, operation, num2, "=", int(num1)*int(num2))
    elif operation == "/":
        print(num1, operation, num2, "=", int(num1)/int(num2))
    else:
        print("Enter a valid input!")