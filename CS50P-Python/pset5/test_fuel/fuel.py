def main():
    fraction = input("Fraction: ").strip()
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    a, b = fraction.split("/")
    a = int(a)
    b = int(b)

    if b == 0:
        raise ZeroDivisionError

    if a > b or a < 0:
        raise ValueError

    percentage = round((a / b) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()