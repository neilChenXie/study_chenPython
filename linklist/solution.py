#!/usr/bin/python

class Solution:
    def deleteDuplicate(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        begin = head
        tail = head.next
        while tail != None:
            if begin.value == tail.value:
                tail = tail.next
            else:
                begin.next = tail
                begin = tail
                tail = tail.next
        begin.next = None
        return head
    def reverseList(self,head):
        if head == None:
            return head
        if head.next == None:
            return head
        one = head
        two = head.next
        three = two.next

        one.next = None
        #long-term reverse
        while three != None:
            two.next = one
            one = two
            two = three
            three = three.next
        two.next = one
        head = two
    def removeNthFromEnd(self, head, n):
        begin = head
        if head == None:
            return head
        if n == 1:
            return head
        tail = begin.next
        i = 1
        while i < n:
            tail = tail.next
            i += 1

        while tail.next != None:
            tail = tail.next
            begin = begin.next
        begin.next = begin.next.next
        return head
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        recA = headA
        recB = headB
        flagA = True
        flagB = True
        while  headA != None and headB != None:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next
            if headA == None and flagA ==True:
                headA = recB
                flagA = False
            if headB == None and flagB == True:
                headB = recA
                flagB = False
        return None

    def recorderlist(self,head):
        #edge case
        if head == None:
            return
        if head.next == None or head.next.next == None:
            return
        #find the middle
        middle = head
        tail = head.next
        while tail.next != None:
            tail = tail.next
            if tail.next != None:
                tail = tail.next
                middle = middle.next
            else:
                break
        print middle.value
        tmpM = middle.next
        middle.next = None
        middle = tmpM
        #reverse the 2n list
        if tail == middle.next:
            tail.next = middle
            middle.next = None
        else:
            nodeOne = middle
            nodeTwo = middle.next
            nodeThree = nodeTwo.next
            middle.next = None
            while nodeThree != None:
                nodeTwo.next = nodeOne
                nodeOne = nodeTwo
                nodeTwo = nodeThree
                nodeThree = nodeThree.next
            nodeTwo.next = nodeOne
        #inter-insert list
        while head != None and tail != None:
            nextH = head.next
            nextT = tail.next
            head.next = tail
            if nextH != None:
                tail.next = nextH
            tail = nextT
            head = nextH
    def rotateRight(self,head):

