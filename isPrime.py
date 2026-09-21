def isprime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if isprime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")