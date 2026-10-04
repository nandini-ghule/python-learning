numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)