get1 = input("Enter any input 1 : ")
get2 = input("Enter any input 2 : ")
try:  # This will attempt to execute the following code in try:
    print("The output is", int(get1)+int(get2))
except Exception as warning:  # If try fails this will display the cause of failure and proceed the program as usual
    print(warning)
""" except:  # If try fails this will display (Alternative message)
    print("Bhai kya daal rha hai!") """
print("This is some important code to be executed")