#!?usr/bin/env python

import random

def main():
    """Start a number guessing gme between 1 - 100."""
    print("Guest the number!")

    x = random.randrange(1, 5)
    guess = None
    
    while x != guess:

        guess = int(input("Pick a number between 1 to 5: "))

        if x == guess:
            print("You genius!")
        else:
            print("Wrong.")
        

main()