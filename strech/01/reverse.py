# -*- encoding: utf-8 -*-
"""
"""

import sys

class Reverse:
        
    def __init__(self, user_args):
        self.text = str(user_args)
    
    def reverse_string(self):
        text = self.text
        return reversed(text)

if __name__ == "__main__":
    user_args = sys.argv[1:]
    
    reverse = Reverse()
    reversed_string = reverse.reverse_string(user_args)
    print(reversed_string)
            


