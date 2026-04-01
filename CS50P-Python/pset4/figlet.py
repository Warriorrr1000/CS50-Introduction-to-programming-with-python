import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
font_list = figlet.getFonts()

def main():
    #Length of arguments.[Error Handling.]
    if len(sys.argv) == 1:
        font = random.choice(font_list)
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid Mode. [Use -f or --f for specifying fonts.]")
        elif sys.argv[2] not in font_list:
            sys.exit("Invalid Font.")
        else:
            font = sys.argv[2]
    else:
        sys.exit("Too few arguments.")

    text = input("Input: ").strip()
    figlet.setFont(font=font)
    print(figlet.renderText(text))




main()