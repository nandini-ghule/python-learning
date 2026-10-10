numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter split position: "))

if len(numbers) > 0:
    k = k % len(numbers)
    first = numbers[:k]
    second = numbers[k:]
    numbers = second + first

print("Split and rotated array:", numbers)