n = int(input("Enter the size of matrix: "))
matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("n x n Matrix:")

for row in matrix:
    print(row)