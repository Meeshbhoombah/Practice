"""
Created by meeshbhoombah

A hangman game created for a homework assignment
for Make School's CS1 class.

Requires the hangman_words.txt file to be in the
same directory.
"""

import random

game_screen = ["""

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
    incorrect_guesses_allowed = 6

    def __init__(self, ):
        self.secret_word = secret_word
        self.secret_li = []
        self.hint_li = []

###### GAME LOGIC #####

print(game_screen[0])
try: 
    input()
except SyntaxError:
    pass


