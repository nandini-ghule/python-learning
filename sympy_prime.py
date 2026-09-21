from sympy import isprime

n = int(input("Enter a number: "))

if isprime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")