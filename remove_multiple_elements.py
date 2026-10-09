numbers = list(map(int, input("Enter numbers: ").split()))
remove = list(map(int, input("Enter elements to remove: ").split()))

for i in remove:
    if i in numbers:
        numbers.remove(i)

print("Updated list:", numbers)