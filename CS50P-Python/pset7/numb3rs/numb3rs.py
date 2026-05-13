# I Kind of Complicated it, Match wasnt working properly probably it was some syntax issue so i did this approach for
# 0-255
import re
import sys



def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if valid := re.search(r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()