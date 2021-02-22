list1 = ["This", "is", "a", "sample", "list"]
# manual joining looks like this
for item in list1:
    print(item, "", end="")

print()  # For adding a new line

# now using the join() method
joined_list = " ".join(list1)
print(joined_list)
