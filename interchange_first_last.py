numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("Updated list:", numbers)