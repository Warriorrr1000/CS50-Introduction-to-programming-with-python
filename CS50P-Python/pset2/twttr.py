def main():
    vowels = ["A","E","I","O","U"]
    inp = input("Input: ")
    for i in inp:
        if i.upper() in vowels:
            print("",end="")
        else:
            print(i,end="")
    print()

main()