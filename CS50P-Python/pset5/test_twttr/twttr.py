def main():
    user_input = str(input("Enter your word: ").strip())
    print(shorten(user_input))

def shorten(word):
    vowels = ["A","E","I","O","U"]
    result = []
    for i in word:
        if i.upper() in vowels:
            pass
        else:
            result.append(i)
    final_result = "".join(result)
    return final_result

if __name__ == "__main__":
    main()