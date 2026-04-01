import emoji

def main():
    emooji = input("INPUT: ").strip()
    emojii = emoji.emojize(emooji,language='alias')
    if emojii == emooji:
        print("Can't find an emoji")
    else:
        print(f"OUTPUT: {emojii}")



main()