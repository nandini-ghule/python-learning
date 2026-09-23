ages = input("Enter the ages of 3 people: ")
ages = ages.split()

print("Number of people:", len(ages))

if len(ages) == 3:
    age = int(ages[0])

    if age >= 18:
        print("The first person is an adult.")
    else:
        print("The first person is a minor.")
else:
    print("Please enter exactly 3 ages.")