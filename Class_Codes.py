# list1 = [5, 6, 37, 41, 55, 15, 30, 132, 150, 1, 10]
# s = 0
# p = 0
# for item in list1:
#     if item > 150:
#         break
#     if item % 5 == 0:
#         s += item
#     if item % 5 != 0:
#         p += item
# print(s, p)


# str1 = "Riya,Rahul,Vanya"
# print(str1[-11:-6])


# def mixing(a, b):
#     new_a = b[:1]+a[3:]
#     new_b = a[:2]+b[2:]
#     return new_a+' '+new_b


# print(mixing('CSE-I', 'NETAJ'))


# def foo(m):
#     if m==0:
#         return 0
#     else:
#         return(m+foo(m-1))

# # print(foo(-5)) # Terminates
# print(foo(11)) # Donot Terminates


# def f(n):
#     s = 0
#     for i in range(1, n+1):
#         if n//i == i and n % i == 0:
#             s = 1
#             return(s % 2 == 1)


# print(f(98)) # False
# print(f(25)) # True


# num = 758689
# count = 0
# while num != 0:
#     if num % 10 == 8:
#         break
#     num //= 10
#     count += 1
# print("Total digits are:", count)


# arr = [2.56, 4, "CSAI", 0.2, True, 1, "/SEC-V", True, 2, None, "/SEC-IV", None, False, 2]
# cntr1, cntr2 = 0, " "
# for i in arr:
#     if (type(i) == int or type(i) == float):
#         cntr1 += i
#     elif(type(i) == str):
#         cntr2 += i
#     elif(i == True):
#         continue
#     else:
#         break
# print(cntr1, cntr2)


# def str_change(str1):
#     return str1[len(str1)-1:]+str1[len(str1)-(len(str1)-1):len(str1)-1]+str1[:len(str1)-(len(str1)-1)]


# print(str_change('COMPUTER'))


# print('the first line',
#       'Plus some continuation')


# x = 'abcd'
# for i in range(len(x)):
#     print(i, end='')


# a = True
# b = True
# c = True
# d = False
# if not a or not b and c or not d:
#     print("CSAI-IV")
# else:
#     print("CSAI-V")


# l1 = [[1], 2, 3, 4]
# l2 = l1
# l3 = l1.copy()
# l4 = l3
# l1[0] = [7]
# l1[1] = [5, 6]
# print(l1, l2, l3, l4)


# print(float("123"*int(input("Enter a number:"))))


# x = ["hello", [2, 4, 6], 10, "python", 20]
# y = x[4:20]
# z = y
# w = x
# x[0] = x[0][:3]+"p!"
# y[0] = 30
# w[0][:3] = "abc" #error
# z[4] = 80
# x[1][2] = 8
# flag = (x[4] == 1)


# n = 6
# for i in range(1, n+1, n % 4):
#     print(i*i, "", end=" ")


# x = [40, 50, 60, 70]
# y = x[1:]
# z = x[2:]
# a = x
# z[0] = 80
# a[2] = 100
# print(y[1])
# print(x[2])
# print(a[2])
# print(z[0])


# i = 0
# while i < 3:
#     print(i, end=" ")
#     i += 1
# else:
#     print(0)


# def fun(x):
#     d = 1
#     n = 0
#     while d <= x:
#         d = d*4
#         n = n+1
#     return (n)


# print(fun(5000))


# a = 7
# b = 2
# print(a/b, a//b)


# def string_ends(str):
#     if len(str) < 2:
#         return ''
#     return str[0:1]+str[-12:8]+str[-6:]


# print(string_ends('Rajeev Kumar Tyagi'))
