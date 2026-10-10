my_list = eval(input("Enter a list of tuples: "))

result = []

for i in my_list:
    if i != ():
        result.append(i)

print("List after removing empty tuples:", result)