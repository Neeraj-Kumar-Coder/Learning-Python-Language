# names = ["Neeraj", "Harry", "Ravi", "Rohan", "Rahul"]
# for items in names:
#     print(items)

# listoflist = [["Bittu", 4], ["Rohan", 3]]
# for name in listoflist:
#     print(name)
# for name, numb in listoflist:
#     print(name, numb)

# print(dict(listoflist))
# for item, rem in dict(listoflist).items():
#     print(item, rem)

# quiz
list_new = ["Anything", 56, "*#&*", 9, 2, 3, 4, "929", "1"]
for item in list_new:
    if str(item).isnumeric() and int(item) > 6:
        print(item)