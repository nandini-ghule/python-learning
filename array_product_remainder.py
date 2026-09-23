numbers = list(map(int, input("Enter numbers: ").split()))
mod = int(input("Enter modulus: "))

product = 1

for number in numbers:
    product = (product * number) % mod

print("Remainder:", product)