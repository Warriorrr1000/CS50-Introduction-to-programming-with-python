import sys
import csv

def main():
    argument_length = len(sys.argv)
    if argument_length > 3:
        sys.exit("Too many command-line arguments")
    elif argument_length < 3:
        sys.exit("Too few command-line arguments")

    data = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    output_data = []
    for i in data:
        last_name , first_name = i["name"].split(",")
        first_name = first_name.strip()
        output_data.append([first_name,last_name,i["house"]])

    try:
        with open(sys.argv[2],"w") as file:
            writer = csv.writer(file)
            writer.writerow(["first","last","house"])
            writer.writerows(output_data)

    except Exception as e:
        sys.exit(f"Error: {e}")

if __name__=="__main__":
    main()