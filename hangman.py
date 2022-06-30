import random
import time

# Initialize the games for the player. The player is asked to enter the name.
print("\nWelcome to Hangman game!\n")
name = input("Please enter your name: ")
print("Hello " + name + "! Good luck!")
time.sleep(1)
print("The game is ready to start!")
time.sleep(1)

# words.txt file should be put in the same directory as the hangman.py file
wordlist_file = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings.

    """
    print("Loading the word list file...")
    inFile = open(wordlist_file, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseword(wordlist):
    """
    wordlist (list): list of words (strings)
    Randomly returns a word from the wordlist
    """
    return random.choice(wordlist)


# define the variables required to run the game:
def main():
    global count
    global display
    global word
    global letters_guessed
    global length
    global game_starter

    # load the wordlist from the words.txt
    WORDLIST = loadwords()
    # all words are transformed to lowercase when selected from the wordlist
    word_original = chooseword(WORDLIST).lower()
    word = word_original
    length = len(word)
    count = 0
    display = '_' * length
    letters_guessed = []
    game_starter = ""

# A loop to re-execute the game when a round ends
def play_loop():
    global game_starter
    game_starter = input("Do You want to play again? Y/y = yes, N/n = no \n")
    while game_starter not in ["y", "n","Y","N"]:
        game_starter = input("Do You want to play again? Y/y = yes, N/n = no \n")
    if game_starter == "y" or game_starter == "Y":
        print("Let's play again!")
        main()
        hangman()
    elif game_starter == "n" or game_starter == "N":
        print("Game over!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global letters_guessed
    global game_starter

    limit = 7 # number of wrong guesses allowed
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    # all guesses are transformed to lowercase when typed by the player
    guess = guess.lower()
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input! Try a letter.\n")
        hangman()

    elif guess in word:
        letters_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in letters_guessed:
        print("Oops! You've already guessed that letter. Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "__|__  / \ \n")
            print("Warning! Wrong guess! " + str(limit - count) + " guesses remained\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |      \n"
                  "  |      \n"
                  "  |       \n"
                  "  |       \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "__|__  / \ \n")
            print("Warning! Wrong guess! " + str(limit - count) + " guesses remained\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "  |       \n"
                 "  |       \n"
                 "  |     O \n"
                 "  |    /|\ \n"
                 "__|__  / \ \n")
           print("Warning! Wrong guess! " + str(limit - count) + " guesses remained\n")

        elif count == 4:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |       \n"
                 "  |       \n"
                 "  |     O \n"
                 "  |    /|\ \n"
                 "__|__  / \ \n")
           print("Warning! Wrong guess! " + str(limit - count) + " guesses remained\n")

        elif count == 5:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |      \n"
                 "  |       \n"
                 "  |       \n"
                 "  |     O \n"
                 "  |    /|\ \n"
                 "__|__  / \ \n")
           print("Warning! Wrong guess! " + str(limit - count) + " guesses remained\n")

        elif count == 6:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |       \n"
                 "  |       \n"
                 "  |     O \n"
                 "  |    /|\ \n"
                 "__|__  / \ \n")
           print("Warning! Wrong guess! " + str(limit - count) + " guess remained\n")

        elif count == 7:
            time.sleep(1)


            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")

            print("You've run out of guesses! You are HANGED!!!\n")
            print("The word was:",letters_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You've'guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()