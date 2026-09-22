#for a given number n, finding the nth fibonacci number

n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    a, b = b, a + b

print("The nth Fibonacci number is:", a)