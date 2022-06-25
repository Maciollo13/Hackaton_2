import random
from hangman_art import hangmanpic

def intro():
    print("""Welcome to the hangman game.
    Your task is to set free a poor man from stretching his neck, by guessing the word that i think of.
    Fortunately you will see the length of the word. Just type the letter this word contains and voila!
    Another man can enjoy their free life. But watch out your bad guesses are limited to 5.
    If u cant guess the word in that time the man will hung, and u will be partially a executioner.
    So go, free some people. (or go on killing spree (-: )""")

def computer_draw():
    with open("words.txt") as fopen:
        content = fopen.readlines()
        return random.choice(content).replace("\n", "")

def player_letter_input():
    player_choice = input("Select a letter: ")
    return player_choice

def word_cover(word):
    covered_word = ""
    for i in word:
        i = "-"
        covered_word += i
    return covered_word

def whole_word_guessing(computer_choice):
    while True:
        player_guess_word = input("Would you like to guess the word? [Y/N]")
        player_guess_word = player_guess_word.casefold()
        if player_guess_word == "y":
            player_guess = input("Guess the word: ")
            if word_guessing(computer_choice, player_guess) == True:
                print("You saved a life!!!")
                return True
            elif word_guessing(computer_choice, player_guess) == False:
                print("Thats not the word!")
                return False

        elif player_guess_word == "n":
            return None
        else:
            print("Input \"Y\" or \"N\"")


def word_guessing(word,player_word):
    flag = word == player_word
    return flag

def main_game(word, player, cover):
    temp_word = list(cover)
    for i, v in enumerate(word):
        if v == player:
            temp_word[i] = v
    return temp_word


def continuation():
    cont = input("Would you like to continue? [Y/N] --> ")
    cont = cont.lower()
    cont = cont[0]
    return cont

def hangman():
    CGREEN = '\33[32m'
    CEND = '\033[0m'
    CRED = '\33[31m'
    intro()
    tries = 5
    killed_people = 0
    saved_people = 0
    hangman_status = 0
    while True:
        print(hangmanpic(hangman_status))
        computer_choice = computer_draw()
        word_covered = word_cover(computer_choice)
        print(f"\nThe word that i think of is \n {word_covered}")
        while tries >= 1:
            print(f"Tries left {tries}")
            player_choice = input("Guess the letter --> ")
            temporary_word = main_game(computer_choice, player_choice, word_covered)
            if temporary_word == list(word_covered):
                print("Opps! You missed.")
                hangman_status += 1
                print(hangmanpic(hangman_status))
                print(*temporary_word)
                tries -= 1
            else:
                print("Bingo! good job.")
                print(hangmanpic(hangman_status))
                print(*temporary_word)
            if temporary_word == list(computer_choice):
                print("You saved a life!!!")
                break
            if whole_word_guessing(computer_choice):
                break
            elif temporary_word == list(computer_choice):

                print(CGREEN+ "You saved a life!!!" +CEND)
                break
            word_covered = temporary_word
            print(*word_covered)
        if tries < 1:
            print("This poor man died because of you.")
            print(CRED+hangmanpic(6)+CEND)
            killed_people += 1
        else:
            saved_people += 1
        cont_button = continuation()
        if cont_button == "n":
            break


hangman()