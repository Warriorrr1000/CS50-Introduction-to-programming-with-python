from datetime import date,datetime
import sys
import inflect

p = inflect.engine()

#As instructions expected me to test other functions beside main , so i seperated some logic into calc_minute and minutes_to_words
def main():
    date_of_birth = input("Date of Birth: ").strip()
    dob = validate_date(date_of_birth)
    current_date = date.today()
    minutes = calc_minutes(current_date,dob)
    print(minutes_to_words(minutes))



def validate_date(date_string, format_string="%Y-%m-%d"):
    try:
        return datetime.strptime(date_string, format_string).date()
    except ValueError:
        sys.exit("Invalid date")

def calc_minutes(current_date,dob):
    return ((current_date-dob).days) * 24 * 60

def minutes_to_words(minutes):
    if minutes in [0,1]:
        min = "minute"
    else:
        min = "minutes"
    return f"{p.number_to_words(minutes,andword='').capitalize()} {min}"

if __name__ == "__main__":
    main()