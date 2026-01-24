def main():
    dollars = dollars_to_float(str(input("How much was the meal? ")))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    floatt = float(d.strip("$"))
    return floatt


def percent_to_float(p):
    p = float(p.strip("%"))
    percentt = p/100
    return percentt


main()