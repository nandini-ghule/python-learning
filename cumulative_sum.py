numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

total = 0

for num in numbers:
    total += num
    print(total)