#! /usr/bin/python

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def get_next(self):
        return self.next
    def get_val(self):
        return self.val
    def set_next(self,n):
        self.next = n
    def set_val(self,x):
        self.val = x

class LinkList:
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self,n):
        new_node = ListNode(n)
        new_node.set_next(self.root)
        self.root = new_node
        self.size += 1
    def append(self,n):
        new_node = ListNode(n)
        nodeTail = self.get_tail()
        if nodeTail == None:
            self.root = new_node
        else:
            nodeTail.set_next(new_node)
        self.size += 1
    def append_node(self,newNode):
        nodeTail = self.get_tail()
        if nodeTail == None:
            self.root = newNode
        else:
            nodeTail.set_next(newNode)
        self.size += 1
    def insert_node(self,newNode):
        newNode.set_next(self.root)
        self.root = newNode
        self.size += 1
    def get_tail(self):
        if self.root == None:
            return None
        nodeGo = self.root
        while nodeGo.get_next() != None:
            print nodeGo.val
            nodeGo = nodeGo.get_next()
        return nodeGo
    def print_all(self):
        r = self.root
        while r != None:
            if r.get_next() != None:
                print str(r.get_val()),"->",
            else:
                print str(r.get_val())
            r = r.get_next()
