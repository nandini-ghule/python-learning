numbers = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element to search: "))

if element in numbers:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")