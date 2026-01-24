def energy_calc(m):
    c = 300000000
    e = m * (c**2)
    return e

def main():
    mass = int(input("Enter the mass[in kg.]: "))
    print(f"{energy_calc(mass)} joules.")

main()