numbers = list(map(int, input("Enter numbers: ").split()))

# Assuming array is both increasing and decreasing initially
increasing = True
decreasing = True

# Comparing each element with the next element
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        increasing = False

    if numbers[i] < numbers[i + 1]:
        decreasing = False

if increasing or decreasing:
    print("Array is monotonic")
else:
    print("Array is not monotonic")