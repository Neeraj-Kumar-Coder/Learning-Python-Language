def prime_teller(number):
    for divisor in range(2, number):
        if not number % divisor:  # checks by diving the number provided which each number
            return False
    return True


number = int(input("Enter the number you want to check for prime status: "))
if prime_teller:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")
