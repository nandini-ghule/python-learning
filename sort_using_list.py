list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

result = []

for i in list2:
    if i in list1:
        result.append(i)

print("Sorted list:", result)