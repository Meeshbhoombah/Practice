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

"""]

class Game(object):
    number_of_guesses = 6

    def __init__(self, ):
        self.secret_word = secret_word
        self.secret_li = []
        self.hint_li = []

    def set_secret_li():
    ''' Split the secret word into a list of letters '''
    
    def set_guess_li():
    ''' Create a list for '''
    
    def check_character():
        
    def get_guess_li():
        
    def decrement_guesses():


