#! /usr/bin/python

import mylist
import solution

if __name__ == "__main__":
    listZero = mylist.LinkList()
    listOne = mylist.LinkList()
    listOne.append(1)
    listOne.append(2)
    listOne.append(3)
    listOne.append(4)
    #listOne.append(9)
    listTwo = mylist.LinkList()
    listTwo.append(7)
    listTwo.append(6)
    listTwo.append(8)
 
    nodeOne = mylist.ListNode(4)
    nodeTwo = mylist.ListNode(5)
    nodeThree = mylist.ListNode(9)
 
    listOne.append_node(nodeOne)
    listOne.append_node(nodeTwo)
    listOne.append_node(nodeThree)
 
    #listTwo.append_node(nodeOne)
    #listTwo.append_node(nodeTwo)
    #listTwo.append_node(nodeThree)

    listOne.print_all()
    listTwo.print_all()

    mySolution = solution.Solution()
    #mySolution.deleteDuplicate(myList.root)
    #mySolution.removeNthFromEnd(myList.root,3)
    #print mySolution.getIntersectionNode(listOne.root,listTwo.root)
    #tmpP = listOne.root
    #mySolution.recorderlist(tmpP)
    #listOne.root = mySolution.rotateRight(listOne.root,3)
    #listOne.root = mySolution.insertionSortList(listOne.root)
    #listOne.root = mySolution.partition(listOne.root,2)
    #listOne.root = mySolution.swapPairs(listOne.root)
    #listOne.root = mySolution.addTwoNumbers(listOne.root, listTwo.root);
    #listOne.root = mySolution.reverseBetween(listOne.root, 2, 7);
    listOne.root = mySolution.deleteDuplicates(listOne.root);


    listOne.print_all()
