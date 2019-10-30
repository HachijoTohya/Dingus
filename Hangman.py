from Wordlist import wordlist
import random
from Wordlist import letrepl
from Wordlist import yesno
from Wordlist import Difficulty
import time

playing = True
lives = 6
diff = Difficulty()
hangword = str(wordlist[random.randrange(0, 1000)]).upper()


def playgame():
    print("\nGuess the word by entering one letter at a time. You have 6 lives. You lose one after an incorrect guess.")
    print("You may guess the entire word, but you will lose if your guess is wrong.\n")
    guesses = []
    tries = 0
    guessing = True
    hangblank = ""
    for letter in hangword:
        hangblank += str(letrepl.get(letter)).upper() + " "
    print(hangblank)
    while guessing:
        guesslist = ""
        if deathcheck(tries, hangblank):
            return
        guess = input("Enter a letter: ").upper()
        # Checks to make sure the guess is valid
        if len(guess) == len(hangword) and guess.isalpha():
            if finalanswer(guess):
                return
        elif len(guess) > len(hangword) and guess.isalpha():
            print(f"\n\nToo many letters! The word is only {len(hangword)} letters long!")
        elif len(hangword) > len(guess) > 1 and guess.isalpha():
            print(f"\n\nNot enough letters! The word is {len(hangword)} letters long!")
        elif redundancycheck(guess, guesses) and guess.isalpha():
            print("\n\nYou already guessed that letter!")
        elif not guess.isalpha():
            print(f"\n\n{guess} is not a valid entry. Please enter a letter or guess the word")
        elif guess in hangword:
            print("\n\nYou guessed a letter!")
            guesses.append(guess)
            hangblank = ""
            #  Creates new display word
            for letter in hangword:
                if letter in guesses:
                    hangblank += letter + " "
                elif letter not in guesses:
                    hangblank += "_ "
        else:
            guesses.append(guess)
            tries += 1
        for item in guesses:
            guesslist += item
        # Display for user
        print(f"\n\n{hangblank}")
        print(f"Tries left:  {lives - tries}")
        print("Guessed Letters:  " + guesslist)


def finalanswer(guess):
    print(f"\n\nAre you sure you want to guess the word {guess}?\nYou will lose the game if you are wrong! (Y/N)")
    final = input(">").lower()
    if yesno.get(final, final) == "yes" and guess == hangword:
        print(f"\n\nYou correctly guessed the word {hangword}! Congrats!")
        return True
    elif yesno.get(final, final) == "yes" and guess != hangword:
        print(f"\n\n{guess} was not the correct answer! The word was {hangword}.")
        return True
    elif yesno.get(final, final) == "no":
        return False
    else:
        print("Please enter 'Yes' or 'no' (Y/N)")


def playagain():
    while True:
        print("Would you like to play again? (Y/N)")
        play = input(">")
        if yesno.get(play, play) == "yes":
            break
        elif yesno.get(play, play) == "no":
            return True
        else:
            print("Please enter 'Yes' or 'No' (Y/N).")


def deathcheck(triesleft, hangblank):
    tools = hangblank.split()
    answer = ""
    for letter in tools:
        answer += letter
    if triesleft == lives and answer == hangword:
        print(f"\n\nYou found the word {hangword}! Congrats!")
        return True
    elif answer == hangword:
        print(f"\n\nYou found the word {hangword}! Congrats!")
        return True
    elif triesleft == lives:
        print(f"\n\nYou have run out of tries. The word was {hangword}.\n\n")
        return True


def redundancycheck(guess, guesses):
    for letter in guesses:
        if guess == letter:
            return True


while playing:
    print("""
Please select a difficulty level or type 'Q' to quit.:

Easy (E): 5 or fewer letters
Medium (M): Between 6 and 8 letters
Hard (H): 9 letters or greater
""")
    while True:
        diffselect = input("> ").lower()
        if yesno.get(diffselect, diffselect) == "easy":
            while not diff.iseasy(hangword):
                hangword = str(wordlist[random.randrange(0, 1000)]).upper()
            break
        elif yesno.get(diffselect, diffselect) == "medium":
            while not diff.ismedium(hangword):
                hangword = str(wordlist[random.randrange(0, 1000)]).upper()
            break
        elif yesno.get(diffselect, diffselect) == "hard":
            while not diff.ishard(hangword):
                hangword = str(wordlist[random.randrange(0, 1000)]).upper()
            break
        elif yesno.get(diffselect, diffselect) == "quit":
            playing = False
            break
        else:
            print(f"{diffselect} is not a valid difficulty level. Please enter 'easy', 'medium', or 'hard'. (E/M/H)")
    if playing:
        playgame()
        if playagain():
            playing = False
print("See you next time!")
time.sleep(2)
