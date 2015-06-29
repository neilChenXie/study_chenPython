#! /usr/bin/python

class listNode:
    def __init__(self,x):
        self.value = x
        self.next = None

class linkList:
    def __init__(self, r = None):
        self.root = r
        self.next = None
    def add(self,n):
        new_node = listNode(n)
        new_node.next = self.root
        self.root = new_node
    def print_all(self):
        r = self.root
        while r != None:
            print str(r.value),"->"
            r = r.next
