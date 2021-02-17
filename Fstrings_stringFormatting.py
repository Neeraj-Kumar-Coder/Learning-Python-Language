# Method 1
me = "Neeraj Kumar"
age = 20
string1 = "This is %s" % me
string2 = "This is %s age %d" % (me, age)
print(string1, string2)

# Method 2
name = "Rahul"
mask = 50
string3 = "Name is {} with mask {}"
string4 = "{1}{0}"
b3 = string3.format(name, mask)
b4 = string4.format(name, mask)
print(b3, b4)

# Method 3: Using f-strings
myself = "Neeraj"
logic = 45
string5 = f"This is {myself} with logic {logic} and lucky number = {7}"
print(string5)