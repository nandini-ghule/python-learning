#finding the sum of squares of first n natural numbers

n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i ** 2

print("Sum of squares:", sum)