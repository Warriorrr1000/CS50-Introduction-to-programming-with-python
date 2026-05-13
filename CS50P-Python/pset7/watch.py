import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if pattern := re.search(r'^(?:<iframe) +?src="https?://(?:www\.)?youtube\.com/embed/([\w_-]{11})"+?',s):
        return f"https://youtu.be/{pattern.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()