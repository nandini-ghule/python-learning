rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print("Enter matrix elements:")
matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

product = 1

for i in range(rows):
    for j in range(columns):
        product *= matrix[i][j]
print("Product of all matrix elements:", product)