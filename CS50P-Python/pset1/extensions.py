def main():
    user_inp = input("File Name: ").lower().strip()

    if user_inp.endswith(".gif"):
        print(f"image/gif")
    elif user_inp.endswith(".jpg") | user_inp.endswith(".jpeg"):
        print(f"image/jpeg")
    elif user_inp.endswith(".png"):
        print(f"image/png")
    elif user_inp.endswith(".pdf"):
        print(f"application/pdf")
    elif user_inp.endswith(".txt"):
        print(f"text/plain")
    elif user_inp.endswith(".zip"):
        print(f"application/zip")
    else:
        print("application/octet-stream")
main()