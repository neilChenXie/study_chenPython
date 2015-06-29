#!/usr/bin/python

class solution:
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
        if headA and headB:
            lenA = 0
            lenB = 0
            beginA = headA
            beginB = headB
            #get length
            while beginA or beginB:
                if beginA:
                    lenA += 1
                    beginA = beginA.next
                if beginB:
                    lenB += 1
                    beginB = beginB.next
            #do adjust


        else:
            return None

