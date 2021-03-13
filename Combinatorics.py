def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number-1)


def combinations(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))


def permutations(n, r):
    return factorial(n)//factorial(n-r)
