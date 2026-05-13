import sys

lines = []
def main():
    argument_length = len(sys.argv)
    if argument_length > 2:
        sys.exit("Too many command-line arguments")
    elif argument_length < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#"):
                    pass
                elif line:
                    lines.append(line)
                else:
                    pass

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(len(lines))

if __name__=="__main__":
    main()