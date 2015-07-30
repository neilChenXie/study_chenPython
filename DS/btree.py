#!/usr/bin/python

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class BTree:
    def __init__(self,newR = None):
        self.root = None
    def addRoot(self, newR):
        self.root = newR
