import sys
from tabulate import tabulate
import csv

def main():
    argument_length = len(sys.argv)
    if argument_length > 2:
        sys.exit("Too many command-line arguments")
    elif argument_length < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    rows = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(rows,headers = "keys",tablefmt = "grid"))


if __name__=="__main__":
    main()