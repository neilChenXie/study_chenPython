#! /usr/bin/python
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next_node = None

newVar = ListNode(2)
newVar.cycleFlag = True
print newVar.cycleFlag
