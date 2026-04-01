#Number guessing game.
import random

def main():
    #For level validity.....
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass
    #Computer Guess....
    computer_guess = random.randint(1,level)
    #Guessing System....
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > computer_guess:
                print("Too large!")
            elif guess < computer_guess:
                print("Too small!!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass


main()