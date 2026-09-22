#finding the sum of cubes of first n natural numbers

n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i ** 3

print("Sum of cubes:", sum)