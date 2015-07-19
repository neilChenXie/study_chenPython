#!/usr/bin/python

class BTreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class MyBTree:
    def __init__(self,newR = None):
        self.root = None
    def addRoot(self, newR):
        self.root = newR
