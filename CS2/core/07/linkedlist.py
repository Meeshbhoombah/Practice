# -*- encoding: utf-8 -*-
"""
linkedlist.py
"""

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:

    def __init__(self, items =  None):
        self.head = None
        self.tail = None

        # if initalalized with items
        if items is not None:
