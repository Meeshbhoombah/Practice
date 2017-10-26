# -*- encoding: utf-8 -*-
"""

"""
import sys
from random import randrange

def rearrange_input(rearrange):
    """

    """
    prev = []
    rearranged = []
    for i in range(len(rearrange)):
        # random int
        val = randrange(0, len(rearrange))
        
        # check if used
        if rearrange[val] in prev:
            i -= 1
            break  
        else:
            # if not used add to rearranged list
            prev.append(val)
            rearranged.append(rearrange[val])
            del rearrange[val]
            
    
    return rearranged

if __name__ == "__main__":
    user_args = sys.argv[1:]
    rearranged = rearrange_input(user_args)
    print(rearranged)

