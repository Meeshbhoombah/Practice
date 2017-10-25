# -*- encoding: utf-8 -*-
""" rearrange words

This module rearranges words passed in by the user via the command line. After 
creating a list of the user's arugments, the module randomly selects words and
rearranges the order in which the words are in.

Example:
    Passing in random words as command-line arguments spits them out in a 
    random order as well::
    
        $ python3 rearrange.py house mouse spouse blouse
        >> spouse house mouse blouse

.. _Source:
    https://github.com/Meeshbhoombah/makeschool/tree/master/cs/cs2/rearrange
"""
import sys
from random import shuffle

class Rearrange:
    
    def __init__(self, user_args):
        self.words_li = user_args
        print(user_args) 


    def new_list(self):
        rearranged_li = self.words_li
        rearranged_li = shuffle(rearranged_li)        
        
        return rearranged_li        


if __name__ == "__main__":
    user_args = sys.argv[1:]
    rearrange = Rearrange(user_args)
    print(rearrange.new_list())

