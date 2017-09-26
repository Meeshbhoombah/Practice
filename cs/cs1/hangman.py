"""
Created by meeshbhoombah

A hangman game created for a homework assignment
for Make School's CS1 class.

Requires the hangman_words.txt file to be in the
same directory.
"""

import random

game_screen = 
["""
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

    Welcome to...    

    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                
    And yes, I do know this is ridculous overkill. Press Enter to play 
    the damn game. (ENTER)

""",
"""
    MENU:
    (F) to play single player (G) to play two player (H) to read the rules

""",
"""
    Rules:
""",
"""
    game over
"""]

# Loads word from file "words.txt" located in the same directory
def loadWord():
   f = open('words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord

###### GAME CLASS ######
class Game(object):
    incorrect_guesses = 0

    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.secret_li = []
        self.hint_li = []

        self.set_hint_li(secret_word)
    def set_hunt_li():
        '''
        Take the length of a word and create underscores for each
        char in the word
        '''

###### GAME LOGIC #####
print(game_screen[0])
try: 
    input()
except SyntaxError:
    pass

preload_word = loadWord()
session = Game(secret_word)

print(game_screen[game_

