#! /usr/bin/python

import mylist
import solution

if __name__ == "__main__":
    listOne = mylist.LinkList()
    listOne.append(1)
    listOne.append(2)
    listOne.append(3)
    listOne.append(4)
    #listOne.append(9)
    listTwo = mylist.LinkList()
    listTwo.insert(12)
    listTwo.insert(20)
    listTwo.insert(17)
 
    nodeOne = mylist.ListNode(1)
    nodeTwo = mylist.ListNode(2)
    nodeThree = mylist.ListNode(3)
 
    #listOne.append_node(nodeOne)
    #listOne.append_node(nodeTwo)
    #listOne.append_node(nodeThree)
 
    listTwo.append_node(nodeOne)
    listTwo.append_node(nodeTwo)
    listTwo.append_node(nodeThree)

    listTwo.print_all()

    mySolution = solution.Solution()
    #mySolution.deleteDuplicate(myList.root)
    #mySolution.removeNthFromEnd(myList.root,3)
    #print mySolution.getIntersectionNode(listOne.root,listTwo.root)
    tmpP = listOne.root
    mySolution.recorderlist(tmpP)

    listOne.print_all()
