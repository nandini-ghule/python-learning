numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = 0

for num in numbers:
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

print("Sum of digits =", total)