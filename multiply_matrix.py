rows1 = int(input("Enter number of rows in first matrix: "))
columns1 = int(input("Enter number of columns in first matrix: "))

print("Enter elements of first matrix:")
matrix1 = []

for i in range(rows1):
    row = []
    for j in range(columns1):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)

rows2 = int(input("Enter number of rows in second matrix: "))
columns2 = int(input("Enter number of columns in second matrix: "))

if columns1 != rows2:
    print("Matrix multiplication is not possible!")

else:
    print("Enter elements of second matrix:")
    matrix2 = []

    for i in range(rows2):
        row = []
        for j in range(columns2):
            element = int(input(f"Enter element [{i}][{j}]: "))
            row.append(element)
        matrix2.append(row)

    result = []

    for i in range(rows1):
        row = []
        for j in range(columns2):
            total = 0
            for k in range(columns1):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    print("Product of the two matrices:")

    for row in result:
        print(row)