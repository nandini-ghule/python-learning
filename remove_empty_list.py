my_list = eval(input("Enter a list: "))

result = []

for i in my_list:
    if i != []:
        result.append(i)

print("List after removing empty lists:", result)