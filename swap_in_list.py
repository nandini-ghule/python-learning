numbers = list(map(int, input("Enter numbers: ").split()))

a = int(input("Enter first position: "))
b = int(input("Enter second position: "))

if 0 <= a < len(numbers) and 0 <= b < len(numbers):
    numbers[a], numbers[b] = numbers[b], numbers[a]
    print("Updated list:", numbers)
else:
    print("Invalid positions")