def main():
    user_inp = input("Greeting: ").lower().strip()
    if user_inp.startswith("hello"):
        print("$0")
    elif user_inp.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
