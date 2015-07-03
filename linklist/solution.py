#!/usr/bin/python
import mylist
class Solution:
    def deleteDuplicate(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        begin = head
        tail = head.next
        while tail != None:
            if begin.val == tail.val:
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
        print middle.val
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
    def rotateRight(self,head,k):
        #edge case
        if head == None or head.next == None or k == 0:
            return head
        #find realK
        listLen = 0
        lenP = head
        while lenP != None:
            listLen += 1
            lenP = lenP.next
        realK = k % listLen
        if realK == 0:
            return head
        #rotate right
        twoPointerCount = realK
        cutH = head
        cutT = head
        while twoPointerCount > 0:
            cutT = cutT.next
            twoPointerCount -= 1
        while cutT.next != None:
            cutH = cutH.next
            cutT = cutT.next
        tmpCutH = cutH.next
        cutH.next = None
        cutH = tmpCutH
        cutT.next = head
        return cutH
    def insertionSortList(self, head):
        #edge case
        if head == None or head.next == None:
            return head
        sortH = head
        sortT = head
        unsortH = head.next
        sortH.next = None
        while unsortH != None:
            ele = unsortH
            unsortH = unsortH.next
            if ele.val <= sortH.val:
                ele.next = sortH
                sortH = ele
            elif ele.val >= sortT.val:
                sortT.next = ele
                ele.next = None
                sortT = ele
            else:
                tmpP = sortH
                while tmpP.next != None and ele.val > tmpP.next.val:
                    tmpP = tmpP.next
                ele.next = tmpP.next
                tmpP.next = ele
        return sortH
    def partition(self, head, x):
        #edge case
        if head == None or head.next == None:
            return head
        dummyHead = mylist.ListNode(0)
        dummyHead.next = None
        bigTail = None
        smallTail = dummyHead
        smallTail.next = None
        cursor = head
        while cursor != None:
            newCur = cursor.next
            if cursor.val < x:
                #append to small
                cursor.next = smallTail.next
                smallTail.next = cursor
                smallTail = cursor
            else:
                #append to big
                if smallTail.next == None:
                    smallTail.next = cursor
                    bigTail = cursor
                else:
                    bigTail.next = cursor
                    bigTail = cursor
                bigTail.next = None
            cursor = newCur
        return dummyHead.next
    def hasCycle(self, head):
        #edge case
        if head == None or head.next == None or head.next.next == None:
            return False
        slow = head
        fast = head
        while fast != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    def detectCycle(self, head):
        if head == None or head.next == None or head.next.next == None:
            return None
        slow = head
        fast = head
        recMeet = None
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                recMeet = fast
                break
        if recMeet == None:
            return None
        newH = head
        while newH != recMeet:
            newH = newH.next
            recMeet = recMeet.next
        return newH
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummyHead = mylist.ListNode(0)
        pre = dummyHead
        oneNode = head
        while oneNode != None and oneNode.next != None:
            twoNode = oneNode.next
            #store next
            newOne = twoNode.next;
            #swap
            pre.next = twoNode
            twoNode.next = oneNode
            oneNode.next = None
            #prepare for next
            pre = oneNode
            oneNode = newOne
        if oneNode != None:
            pre.next = oneNode
        return dummyHead.next
    def addTwoNumbers(self, l1, l2):
        c = 0
        rvH = l1
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        while True:
            tmpRes = l1.val + l2.val + c
            if tmpRes >= 10:
                l1.val = tmpRes % 10
                c = 1
            else:
                l1.val = tmpRes
                c = 0
            if l1.next != None and l2.next != None:
                l1 = l1.next
                l2 = l2.next
            else:
                break
        if l2.next != None:
            l1.next = l2.next
            l2.next.val += c
            l2 = l2.next
            while l2.val == 10:
                l2.val %= 10
                if l2.next != None:
                    l2.next.val += 1
                    l2 = l2.next
                else:
                    newNode = mylist.ListNode(1)
                    l2.next = newNode
        elif l1.next != None:
            l1.next.val += c
            l1 = l1.next
            while l1.val == 10:
                l1.val %= 10
                if l1.next !=None:
                    l1.next.val += 1
                    l1 = l1.next
                else: 
                    newNode = mylist.ListNode(1)
                    l1.next = newNode
        elif c == 1:
            newNode = ListNode(1)
            l1.next = newNode
        return rvH
    def reverseBetween(self, head, m, n):
        #edge case
        mnDiff = n - m
        if mnDiff == 0:
            return head
        #find H and T
        dummyHead = mylist.ListNode(0)
        dummyHead.next = head
        h = head
        t = head
        i = 0
        while i < mnDiff:
            t = t.next
            i += 1
        i = 1
        pre = dummyHead
        while i < m:
            h = h.next
            t = t.next
            pre = pre.next
            i += 1
        #reverse
        pre.next = t
        one = h
        two = h.next
        three = two.next
        h.next = t.next
        while two != t:
            two.next = one
            one = two
            two = three
            if three != None:
                three = three.next
        two.next = one
        return dummyHead.next
    def deleteDuplicates(self, head):
        #edge case
        if head == None or head.next == None:
            return head
        dummyHead = mylist.ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        anchor = head
        cursor = head.next
        while cursor != None:
            if cursor.val != anchor.val:
                if anchor.next == cursor:
                    pre = pre.next
                    pre.next = cursor
                    anchor = cursor
                else:
                    pre.next = cursor
                    anchor = cursor
            cursor = cursor.next
        if anchor.next != None:
            pre.next = None
        return dummyHead.next
