#! /usr/bin/python

if __name__ == "__main__":
   myList = linkList()
   myList.add(10)
   myList.add(10)
   myList.add(8)
   myList.add(8)
   mySolution = solution()
   #mySolution.deleteDuplicate(myList.root)
   mySolution.removeNthFromEnd(myList.root,3)
   myList.print_all()
