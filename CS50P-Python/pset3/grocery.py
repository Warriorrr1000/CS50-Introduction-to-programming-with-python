#This one is extremely incorrect... i'm writing code after some months,so kind of...
def main():
    d = {}
    grocery_items = {}
    while True:
        try:
            inp = input("").upper().strip()
            if inp in d:
                number = d[inp]
                d[inp] = number + 1
            else:
                d[inp] = 1
            sorted_dict = sorted(d)
            for item in sorted_dict:
                i = d[item]
                grocery_items[item] = i
        except EOFError:
            break
    for _ in grocery_items:
        print(f"{grocery_items[_]} {_}")


main()