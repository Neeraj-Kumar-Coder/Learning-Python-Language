# map() function: #######################

# sample_list = ["12", "42", "34", "87"]

# normal method

# for i in range(len(sample_list)):
#     sample_list[i] = int(sample_list[i])
# print(sample_list[1]+1)

# using map() method

# result = list(map(int, sample_list))
# print(result[2]+1)

# example 1
# num = [1, 2, 3, 4, 5]


# def sq(n):
#     return n*n


# square = list(map(sq, num))  # Using function in the map()
# print(square)

# square1 = list(map(lambda x: x*x, num))
# print(square1)

# example 2
def square(n):
    return n*n


def cube(n):
    return n*n*n


func = [square, cube]
for i in range(5):
    var = list(map(lambda x: x(i), func))
    print(var)


# filter() function:######################

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_greater(num):
    return num > 5


parsed = list(filter(is_greater, list_1))
print(parsed)
