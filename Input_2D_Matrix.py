row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
temp_list = []
final_list = []
for count in range(row*column):
    value = int(input("Enter the value: "))
    temp_list.append(value)
    if not (count+1) % column:
        # final_list.append(temp_list) # This will append a pointer to the temp_list (shallow copy)
        final_list.append(temp_list.copy())
        temp_list.clear()

print(final_list)
