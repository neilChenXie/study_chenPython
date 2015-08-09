#!/usr/bin/python

#standard lib
import os
import sys

sys.path.append(os.path.abspath('./DS'))

#data structure
import linklist
import btree

#related solution
#import dc
#import dp
import arysol

#list test
#listOne = mylist.LinkList()
#listOne.append(-10)
#listOne.append(-3)
#listOne.append(0)
#listOne.append(5)
#listOne.append(9)
#-10 -> -3 -> 0 -> 5 -> 9

#BTree test
#newR = myBTree.BTreeNode(1)
#node1 = myBTree.BTreeNode(2)
#node2 = myBTree.BTreeNode(3)
#node3 = myBTree.BTreeNode(4)
#node4 = myBTree.BTreeNode(5)
#node5 = myBTree.BTreeNode(3)
#node6 = myBTree.BTreeNode(4)
#bTree = myBTree.MyBTree(newR)
#newR.left = node1
#newR.right = node2
#node1.left = node3
#node1.right = node4
#node2.right = node5
#node2.left = node6
#    1
#  2   3
# 4 5 4 3

#string input
a = [3,4,6,0,3,7,5,8,2,9,1,6,6,2]
##solution
mysolu = arysol.Solution()
print mysolu.maxProfit(a)
