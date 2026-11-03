rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
matrix1 = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)

print("Enter elements of second matrix:")
matrix2 = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix2.append(row)

result = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)

print("Difference of the two matrices:")

for row in result:
    print(row)