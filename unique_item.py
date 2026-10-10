arr = [5, 5, 3, 6, 3, 1, 1]

for i in arr:
    if arr.count(i) == 1:
        print("Unique element:", i)
        break