def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #Rule 1: There should be atleast two letters at start.
    if not s[:2].isalpha():
        return False
    #Rule 2: Length of plate should be between 2-6
    if len(s) < 2 or len(s) > 6:
        return False
    #Rule 3:
    number_started = False
    for char in s:
        if char.isdigit():
            if char == "0" and number_started == False:
                return False
            else:
                number_started = True
        else:
            if number_started == True:
                return False
    #Rule 4: Only Letters and Numbers are allowed
    if not s.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()