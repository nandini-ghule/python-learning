rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

k = int(input("Enter column number (starting from 0): "))

if k < 0 or k >= columns:
    print("Invalid column number.")

else:
    kth_column = []

    for i in range(rows):
        kth_column.append(matrix[i][k])

    print("Kth column:", kth_column)