def main():
    months = {
        "January": 1, "February": 2, "March": 3,
        "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9,
        "October": 10, "November": 11, "December": 12
    }

    while True:
        try:
            inp = input("Date: ").strip()

            # Case 1: MM/DD/YYYY
            if "/" in inp:
                month, day, year = inp.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            # Case 2: Month DD, YYYY
            else:
                inp = inp.replace(",", "")
                month, day, year = inp.split()
                month = months[month.title()]
                day = int(day)
                year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                break

        except (ValueError, KeyError):
            pass

    print(f"{year}-{month:02}-{day:02}")


main()