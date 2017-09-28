"""
Created by @meeshbhoombah

A terminal based Hangman for Make School's 
CS1 class.

Requires the hangman_words.txt file to be 
in the same directory.
"""

import os
import random
import requests
import re
import sys
import threading

from bs4 import BeautifulSoup

game_screen = ["""
    Welcome to...    

    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                
    And yes, I do know this is  overkill. Press Enter to play the damn 
    game. (ENTER)
""",
"""
    HOW TO PLAY  =====================================================
    The computer will generate a secret word from online or from the 
    Make School homepage (you get to decided do you feel special yet?)
    
    You will be prompted to make a guess
      - For every INCORRECT guess you gain a body part
      - For every CORRECT guess you move one 'char' closer to 
        'char'ishing your freedom once again

    (G)enerate the word locally OR (S)crape from Make School
""",
"""
    game over
"""]

# WE OUT HERE THREADING ================================================
def worker(url):
    '''Thread worker function, in this case the worker handles the
    Beautiful Soup logic in the background while the user goes through
    game set up.
    ''' 

# GENERATE SECRET WORD  ================================================
def generate_local_corpus():
    '''Loads word from file "words.txt" located in the same directory'''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = wordsList[0].split(' ')
    secret_word = random.choice(wordsList)
    return secret_word
 
def generate_online_corpus():
    '''Generates word from https://www.makeschool.com/ using Beautiful Soup'''
    SOURCE_URL = "https://www.makeschool.com/"
    
    soup = BeautifulSoup(requests.get(SOURCE_URL).text, 'html.parser')
    [s.extract() for s in soup('script')]
    parsed_text = re.sub('[^A-Za-z0-9]+', ' ', soup)
    parsed_text_li = text.split("")
    
    chosen_word = random.choice(parse_text_li)
    secret_word = chosen_word.lower()
    return secret_word
     
# GAME CLASS ===========================================================
class Game(object):
    incorrect_guesses_remaining = 6

    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.hint_li = []
        
        self.set_hint_li(secret_word)

    def set_hint_li(self, secret_word):
        '''Create an array of underscores with as long as secret_word'''
        for i in len(secret_word):
            hint_li.append("_")
        
    def incorrect_guess(self):
        '''Decrement guess, if no guesses left, end the game'''
        if incorrect_guesses_remaining == 0:
            self.game_lost()
        else:
            incorrect_guesses_remaining -= 1
        
    def correct_guess(self, secret_word):
        guess_found_at = [n for n in xrange(len(secret_word)) if secret_word.find(user_guess, n) == n]
        for i in len(char_found_at):
            hint_li[char_found_at[i]] = user_guess

        if "_" not in hint_li:
            self.game_won()

    def game_lost(self):
        print("You lost. REST IN PEACE.")
        sys.exit(); 

    def game_won(self):
        print("Well done. You won! God bless.")
        sys.exit();

# GAME LOGIC ===========================================================
def main():
    menu_option_invalid = True
    in_game = False

    print(game_screen[0])
    try: 
        input()
    except SyntaxError:
        pass

    print(game_screen[1])
    while(menu_option_invalid):
        menu_option = input()
        if menu_option == "g":
            word = generate_local_corpus()
            invalid = False
            break
        elif menu_option == "s":
            word = generate_online_corpus()
            invalid = False
            pass
        else:
            print("You have to choice. (G)enerate locall or (S)crape Word")

    hangman = Game(secret_word = word)

    in_game = True
    while in_game:
        print(hint_li)
        user_guess = input("Please guess a word or letter: ")
        
        if user_guess == secret_word:
            won_game()
        elif len(user_guess) == 1:
            if user_guess in secret_word:
                correct_guess()
                print("Correct_guess")
                pass
            else:
                incorrect_guess()
                print("Incorrect guess :(")
                pass
        else:
            lost_game()
         
