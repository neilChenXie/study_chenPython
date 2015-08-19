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
#import arysol
#import stacksol
#import greedysol
#import hashsol
#import treesol
#import backtracksol
#import strsol
#import bitsol
#import sortsol
import specialsol

#list test
#listOne = mylist.LinkList()
#listOne.append(-10)
#listOne.append(-3)
#listOne.append(0)
#listOne.append(5)
#listOne.append(9)
#-10 -> -3 -> 0 -> 5 -> 9

#BTree test
newR = btree.TreeNode(4)
node1 = btree.TreeNode(2)
node2 = btree.TreeNode(6)
node3 = btree.TreeNode(1)
node4 = btree.TreeNode(3)
node5 = btree.TreeNode(7)
node6 = btree.TreeNode(5)
bTree = btree.BTree(newR)
newR.left = node1
newR.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node2.left = node6
#    1
#  2   3
# 4 5 4 3
#bTree.BFS(newR)

#string input
#s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
#t = "bddabdcae"
#ary input
a = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
#number input
##solution
mysolu = specialsol.Solution()
print mysolu.canFinish(10,a)
#print a
