rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix = []

print("Enter string elements: ")

for i in range(rows):
    row = []
    for j in range(columns):
        element = input(f"Enter element [{i}][{j}]: ")
        row.append(element)
    matrix.append(row)

result = []

for j in range(columns):
    string = ""
    for i in range(rows):
        string += matrix[i][j]
    result.append(string)

print("Vertically concatenated matrix:", result)