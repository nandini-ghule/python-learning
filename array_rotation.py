numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation count: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Rotated array:", rotated)

# Rotating the original array k positions to the left.