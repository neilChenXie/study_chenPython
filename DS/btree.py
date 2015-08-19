#!/usr/bin/python
import Queue

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
    def BFS(self, node):
        bfsQ = Queue.Queue()
        bfsQ.put(node)
        count = 1
        nextc = 0
        while bfsQ.qsize() > 0:
            tmp = bfsQ.get()
            print tmp.val,
            count -= 1
            if tmp.left:
                bfsQ.put(tmp.left)
                nextc += 1
            if tmp.right:
                bfsQ.put(tmp.right)
                nextc += 1
            if count == 0:
                print
                count = nextc
                nextc = 0
        
