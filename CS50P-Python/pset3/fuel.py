def main():
    while True:
        inp = input("Fraction: ").strip()
        x , y = inp.split("/")
        percent = percentage_validity(x,y)
        if percent == False:
            continue

        if percent <= 1:
            print("E")
            break
        elif percent >= 99:
            print("F")
            break
        else:
            print(f"{percent}%")
            break

def percentage_validity(a,b):
    try:
        a = int(a)
        b = int(b)

        if a < 0:
            raise Exception
        elif a == 0:
            raise ZeroDivisionError
        percentage = round(a/b*100)
        return int(percentage)
    except Exception:
        return False



main()