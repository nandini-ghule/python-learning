# start number should be less than end number

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    if num < 0:
        print(num)
