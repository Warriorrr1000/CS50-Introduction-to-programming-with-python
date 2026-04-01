from random import randint


def main():
    level = get_level()
    sum_count = 0
    score = 0
    while sum_count != 10:
        x = generate_integer(level)
        y = generate_integer(level)
        sum_count += 1
        error_count = 0
        while True:
            answer = x + y
            if error_count == 3:
                print(f"{x} + {y} = {answer}")
                error_count = 0
                break
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer != answer:
                    error_count += 1
                    print("EEE")
                else:
                    score += 1
                    break
            except ValueError:
                error_count += 1
                print("EEE")
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
            else:
                raise ValueError
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        a = randint(0,9)
    elif level == 2:
        a = randint(10,99) 
    else:
        a = randint(100,999)
    return a

if __name__ == "__main__":
    main()