import sys
from PIL import Image,ImageOps
import os

def main():
    valid_ext = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    arg_len = len(sys.argv) #Argument Length.
    if arg_len > 3:
        sys.exit("Too many command-line arguments")
    elif arg_len < 3:
        sys.exit("Too few command-line argument")
    elif ext1 not in valid_ext:
        sys.exit("Invalid Input")
    elif ext2 not in valid_ext:
        sys.exit("Invalid output")
    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        input_image = Image.open(sys.argv[1])
        size = shirt.size
        input_image = ImageOps.fit(input_image,size)
        input_image.paste(shirt,shirt)
        input_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__=="__main__":
    main()