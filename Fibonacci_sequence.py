# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
def Fibonacci_recursion(number):
    if number == 1 or number == 2:
        return number-1
    else:
        return Fibonacci_recursion(number-1)+Fibonacci_recursion(number-2)


def Fibonacci_iteration(number):
    if number == 1 or number == 2:
        return number-1
    else:
        previous = 0
        result = 1
        while(number-2):
            temp = result
            result += previous
            previous = temp
            number -= 1
    return result

# OR


def Fibonacci_iteration_short(number):
    a, b = 0, 1
    for _ in range(1, number):
        a, b = b, a+b
    return a


print(Fibonacci_recursion(10))
print(Fibonacci_iteration(10))
print(Fibonacci_iteration_short(10))
