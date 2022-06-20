#!/usr/bin/env python

import random

def main():
    """Start a guess the periodic elements and numbers"""
    print("Guess the periodic elements!")

    elements  = [
        "beryllium",
        "magnesium",
        "calcium",
        "strontium",
        "rarium",
        "radium"
    ]

    x = random.choice(elements)
    print (x)
    guess = None

    while x != guess:

        guess = str(input("Namakan logam alkali tanah? "))

        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()
