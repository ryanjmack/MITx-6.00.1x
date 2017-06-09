"""
Created on Wed Jun  7 09:36:06 2017

@author: ryanjmack

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive)
and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess\
too high or too low? Using bisection search, the computer will guess the user's secret number!

Illustrates the 'Bisection Search' Algorithm
"""

high = 0
low = 100
middle = int((high + low) / 2)

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number {}?".format(middle))
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess \
                   is too low. Enter 'c' to indicate I guessed correctly. ")

    if check == "h":
        low = middle
    elif check == "l":
        high = middle
    elif check == "c":
        print("Game over. Your secret number was: {}".format(middle))
        break;
    else:
        print("Sorry, I did not understand your input.")

    middle = int((high + low) / 2)
