# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far

    output: string, comprised of letters and underscores that represents
            what letters in secretWord have been guessed so far.
    '''
    output = ""

    for char in secretWord:
        if char not in lettersGuessed:
            output += "_ "
        else:
            output += char

    return output



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far

    returns: string, comprised of letters that represents what letters have not
             yet been guessed.
    '''
    output = string.ascii_lowercase

    for char in lettersGuessed:
        output = output.replace(char, "")

    return output

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game of hangman!")
    print("I am thinking of a word that contains {} letters".format(len(secretWord)))
    print("-----------")

    lettersGuessed = []
    guesses = 8

    # tell users how many guesses they have left, and what letters they can use
    while guesses > 0:
        if guesses > 1:
            print("You have {} guesses left!".format(guesses))
        else:
            print("You have 1 guess left!")
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))

        # get user's guess
        guess = (input("Please guess a letter: ")).lower()

        # checks
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", end="")
        elif guess not in secretWord:
            print("Oops! That letter is not in my word: ", end="")
            guesses -= 1
        elif guess.isalpha() and len(guess) == 1:
            print("Good guess: ", end="")
        lettersGuessed.append(guess)

        # print secretWord with letters that user guessed correctly
        print("{}\n-----------".format(getGuessedWord(secretWord, lettersGuessed)))

        # check to see if the player won
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            return

    print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
