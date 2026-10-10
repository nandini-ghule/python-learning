numbers = list(map(int, input("Enter numbers: ").split()))

unique = {}

for num in numbers:
    if numbers.count(num) == 1 and num not in unique:
        unique[num] = True

print("unique:", list(unique.keys()))