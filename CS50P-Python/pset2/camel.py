camel_case = input("Camel Case: ")
print("snake_case: ",end="")
for i in camel_case:
    if i.isupper():
        i = i.lower()
        print("_" + i,end="")
    else:
        print(i,end="")
print()