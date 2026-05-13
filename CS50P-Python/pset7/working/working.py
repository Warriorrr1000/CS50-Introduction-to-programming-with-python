import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",s):
        return f"{AM_PM_to_24(time.group(1),time.group(2),time.group(3))} to {AM_PM_to_24(time.group(4),time.group(5),time.group(6))}"
    else:
        raise ValueError

def AM_PM_to_24(hour,minute,period):
    hour = int(hour)
    if minute == None:
        minute = 0
    minute = int(minute)
    if minute == 60:
        hour += 1
    if not (1 <= hour <= 12 and 0 <= minute < 60):
        raise ValueError
    if period == "AM":
        if hour == 12:
            hour = 0

    elif period == "PM":
        if hour != 12:
            hour += 12


    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()