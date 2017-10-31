# -*- encoding: utf-8 -*-
""" rearrange words

this module rearranges words passed in by the user via the command line. after 
creating a list of the user's arugments, the module randomly selects words and
rearranges the order in which the words are in.

example:
    passing in random words as command-line arguments spits them out in a 
    random order as well::
    
        $ python3 rearrange.py house mouse spouse blouse
        >> spouse house mouse blouse

.. _source:
    https://github.com/meeshbhoombah/makeschool/cs2
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

