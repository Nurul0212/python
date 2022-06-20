#!?usr/bin/env python

import random

def main():
    """Start a number guessing gme between 1 - 100."""
    print("Guest the number!")

    #x = random.randint(1, 100)
    x = random.gauss(1,5)
    print(x)
    guess = None
    
    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("Cheater!")
        else:
            print("Good")
       # elif x > guess:
            #print("Try a bigger number.")
        #elif x < guess:
            #print("Try a smaller number.")

main()