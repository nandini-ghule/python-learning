numbers = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter chunk size: "))

if n > 0:
    for i in range(0, len(numbers), n):
        print(numbers[i:i + n])
else:
    print("Chunk size must be positive")