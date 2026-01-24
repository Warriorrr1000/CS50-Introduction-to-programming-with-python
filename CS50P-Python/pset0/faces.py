def convert(inp):
    inp1 = inp.replace(":)","🙂")
    inp1 = inp1.replace("(:","🙂")
    inp1 = inp1.replace(":(","🙁")
    inp1 = inp1.replace("):","🙁")
    return inp1


def main():
    inp = str(input())
    print(convert(inp))


main()