"""
Created by @meeshbhoombah

A terminal based Hangman for Make School's 
CS1 class.

Requires the hangman_words.txt file to be 
in the same directory.
"""

import random, os, requests, re
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
    Rules:
""",
"""
    1
""",
"""
    2
""",
"""
    3
""",
"""
    4
""",
"""
    5
""",
"""
    game over
"""]

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
    
    secret_word = random.choice(parse_text_li)
    return secret_word.lower()

# GAME CLASS ===========================================================
class Game(object):
    incorrect_guesses_allowed = 6

    def __init__(self, secret_word):
        self.secret_word = secret_word

        
        self.hint_li = []

    def set_hint_li(self, secret_word):
        

# GAME LOGIC ===========================================================
print(game_screen[0])
try: 
    input()
except SyntaxError:
    pass

print(game_screen[1])
invalid = False
while(invalid):
    menu_option = input()
    if menu_option == "p":
    
    else if menu_option == "s":

    else if menu_option == "r":
    
    else:
        print("Your choice is invalid!")
        
