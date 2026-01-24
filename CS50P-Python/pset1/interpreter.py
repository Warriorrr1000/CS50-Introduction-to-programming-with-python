def main():
    user_inp = input("Enter your expression: ")
    x,y,z = user_inp.split(" ")
    x = int(x)
    z  = int(z)
    print(float(solve(x,y,z)))

def solve(x,y,z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        if z == 0:
            return "Cannot be divided by zero."
        else:
            return x / z
    else:
        return "Invalid Operator."

main()