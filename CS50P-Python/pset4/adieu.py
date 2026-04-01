import inflect

p = inflect.engine()
def main():
    names = []
    while True:
        try:
            user_input = input("Name:").strip().title()
            names.append(user_input)
        except EOFError:
            print()
            print(f"Adieu, adieu, to {p.join(names)}")
            break

main()