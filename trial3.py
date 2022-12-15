dict1 = {
"Fruit" : "Apple" ,
"Vegetable" : "Potato",
"Brand" : "Bee Virtual",
"Country" : "Nepal"
}

user_input = int(input("Enter a number: "))
for index, keys in enumerate(list(dict1.keys())):
    if user_input == index:
        del dict1[keys]

print(dict1)