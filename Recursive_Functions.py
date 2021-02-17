def factorial_recursive(number):
    if number == 1:
        return 1
    else:
        return number*factorial_recursive(number-1)


def factorial_iterative(number):
    result = 1
    for i in range(number):
        result *= i+1
    return result


print(factorial_recursive(10))
print(factorial_iterative(10))
