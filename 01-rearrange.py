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

def rearrange_input(rearrange):
    r = rearrange
    shuffle(r)
    return r


if __name__ == "__main__":
    user_args = sys.argv[1:]
    rearranged = rearrange_input(user_args)
    print(rearranged)

