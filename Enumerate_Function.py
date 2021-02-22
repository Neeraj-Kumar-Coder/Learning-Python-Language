# A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
# Python eases the programmer’s task by providing a built-in function enumerate() for this task.
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
l1 = ["Eat", "Code", "Repeat"]
s1 = "Neeraj Kumar"
for num, item in enumerate(l1):
    print(num, item, end=" ")
for num, item in enumerate(s1):
    print(num, item, end=" ")
print()
print(list(enumerate(l1)))
print(list(enumerate(s1)))
