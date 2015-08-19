import pdb
import linklist
import btree

class Solution:
    def countNodes(self, root):
        l = root
        r = root
        ll = 0
        rl = 0
        while r != None:
            r = r.right
            rl += 1
        while l != None:
            l = l.left
            ll += 1
        if rl == ll:
            return pow(2,rl) - 1
        else:
            return self.countNodes(r.right) + self.countNodes(l.left)
#    def isValidBST(self, root):
#        return 
#    def __doValid(self, node, rangeMax, rangeMin):
#        if (rangeMax == None and rangeMin == None) or (rangeMax == None and node.val > rangeMin) or (node.val > rangeMin and node.val < rangeMax):
#            return self.__doValid(node.right, rangeMax, node.val) and self.__doValid(node.left, node.val, rangeMin)
#        else:
#            return False

#    def kthSmallest(self, root, k):
#        '''find the kth smallest in BST'''
#        count = 0
#        dfsStack = []
#        while count < k:
#            if root.left != None:
#                dfsStack.append(root)
#                root = root.left
#            elif root.right != None:
#                count += 1
#                if count < k:
#                    root = root.right
#                else:
#                    return root
#            else:
#                count += 1
#                while root.right == None and count < k:
#                    root = dfsStack.pop()
#                    count += 1
#                if count == k:
#                    return root
#                else:
#                    root = root.right
#        return root
#    def lowestCommonAncestor(self, root, p, q):
#        '''find the lowest common ancestor of BST'''
#        while root != None:
#            if root.val > p.val and root.val > q.val:
#                root = root.left
#            elif root.val < p.val and root.val < q.val:
#                root = root.right
#            else:
#                return root
#    def lowestCommonAncestorII(self, root, p, q):
#        '''find LCA of any BT'''
#        of = False
#        recLen = 0
#        lca = None
#        dfsStack = []
#        while root != None:
#            if root.right != None:
#                dfsStack.append(root)
#            if root == p:
#                if not of:
#                    of = True
#                    recLen = len(dfsStack)
#                    lca = root
#                else:
#                    return lca
#            elif root == q:
#                if not of:
#                    of = True
#                    recLen = len(dfsStack)
#                    lca = root
#                else:
#                    return lca
#            #DFS continue
#            if root.left != None:
#                root = root.left
#            else:
#                root = dfsStack.pop()
#                if len(dfsStack) < recLen:
#                    lca  = root
#                    recLen = len(dfsStack)
#                root = root.right
#        return lca


#    def dfsNoRecur(self,root):
#        if root == None:
#            return
#        nodeStack = []
#        rec = {}
#        nodeStack.append(root)
#        tmp = nodeStack[-1]
#        rec[id(tmp)] = True
#
#        print root.val
#        while tmp != None:
#            if tmp.left != None and not id(tmp.left) in rec:
#                print tmp.left.val
#                nodeStack.append(tmp.left)
#                rec[id(tmp.left)] = True
#            elif tmp.right != None and not id(tmp.right) in rec:
#                print tmp.right.val
#                nodeStack.append(tmp.right)
#                rec[id(tmp.right)] = True
#            else:
#                tmp = nodeStack.pop()
#            if len(nodeStack) == 0:
#                return
#            tmp = nodeStack[-1]
#    def isBalanced(self, root):
#        rv = self.getDepth(root)
#        print rv
#        if rv == -2:
#            return False
#        return True
#    def getDepth(self,root):
#        if root == None:
#            return -1
#        lenL = self.getDepth(root.left)
#        lenR = self.getDepth(root.right)
#        res = abs(lenL - lenR)
#
#        if res > 1 or lenL == -2 or lenR == -2:
#            return -2
#
#        print "the %d node has depth diff %d" % (root.val, res)
#        return lenL + 1 if lenL > lenR else lenR + 1
#
#    def isSymmetric(self, root):
#        if root == None:
#            return True
#        rv = self.recurCheck(root.left, root.right)
#        print rv
#        if rv == -1:
#            return False
#        return True
#    def recurCheck(self,left,right):
#        if left == right == None:
#            return 0
#        elif left == None or right == None:
#            return -1
#        elif left.val == right.val:
#            if self.recurCheck(left.left, right.right) == -1:
#                return -1
#            if self.recurCheck(left.right, right.left) == -1:
#                return -1
#            return 0
#        else:
#            return -1
#    def isSymmetricNoRecur(self, root):
#        if root == None or root.right == root.left == None:
#            return True
#        if root.right == None or root.left == None or root.right.val != root.left.val:
#            return False
#        nodeSL = []
#        nodeSR = []
#        recL = {}
#        recR = {}
#        nodeSL.append(root.left)
#        nodeSR.append(root.right)
#        tmpL = nodeSL[-1]
#        tmpR = nodeSR[-1]
#        while tmpL != None and tmpR != None:
#            if tmpL.left != None and tmpR.right != None and not id(tmpL.left) in recL and not id(tmpR.right) in recR:
#                if tmpL.left.val != tmpR.right.val:
#                    return False
#                recL[id(tmpL.left)] = True
#                recR[id(tmpR.right)] = True
#                nodeSL.append(tmpL.left)
#                nodeSR.append(tmpR.right)
#            elif tmpL.right != None and tmpR.left != None and not id(tmpL.right) in recL and not id(tmpR.left) in recR:
#                if tmpL.right.val != tmpR.left.val:
#                    return False
#                recL[id(tmpL.right)] = True
#                recR[id(tmpR.left)] = True
#                nodeSL.append(tmpL.right)
#                nodeSR.append(tmpR.left)
#            elif tmpL.right != tmpR.left or tmpL.left != tmpR.right:
#                if tmpL.left == None or tmpR.right == None or tmpL.right == None or tmpR.left == None:
#                    return False
#                elif tmpL.right.val != tmpR.left.val or tmpL.left.val != tmpR.right.val:
#                    return False
#            else:
#                nodeSL.pop()
#                nodeSR.pop()
#
#            if nodeSL.__len__() == nodeSR.__len__() == 0:
#                return True
#            elif nodeSL.__len__() == nodeSR.__len__() != 0:
#                tmpL = nodeSL[-1]
#                tmpR = nodeSR[-1]
#            else:
#                return False
#    def isSameTree(self, p, q):
#        if p == q == None:
#            return True
#        return self.compare(p,q)
#
#    def compare(self,pNode,qNode):
#        if pNode == qNode == None:
#            return True
#        elif pNode == None or qNode == None:
#            return False
#        elif pNode.val == qNode.val:
#            if self.compare(pNode.left,qNode.left) and self.compare(pNode.right,qNode.right):
#                return True
#            return False
#        else:
#            return False
#
#    tmp = 0
#    min = None
#    def minDepth(self, root):
#        self.getMinDepth(root)
#        if self.min == None:
#            self.min = 1
#        return self.min
#    def getMinDepth(self, root):
#        self.tmp += 1
#        if root == None:
#            self.tmp -= 1
#            self.min = self.min if (self.min <= self.tmp and self.min != None) or (self.tmp == 1) else self.tmp
#        else:
#            self.getMinDepth(root.left)
#            self.getMinDepth(root.right)
#        return
#    def BFS(self, root):
#        BFSQ = []
#        res = []
#        rowTmp = []
#        nextStart = 0
#        cursor = 0
#        #start
#        BFSQ.append(root)
#        nextStart = len(BFSQ)
#        while cursor < len(BFSQ):
#            if cursor == nextStart:
#                #create new tmp
#                res.append(list(rowTmp))
#                rowTmp = []
#                nextStart = len(BFSQ)
#            #get next
#            node = BFSQ[cursor]
#            rowTmp.append(node.val)
#            if node.left != None:
#                BFSQ.append(node.left)
#            if node.right != None:
#                BFSQ.append(node.right)
#            cursor += 1
#        res.append(list(rowTmp))
#        return res
#    def levelOrderBottom(self, root):
#        if root == None:
#            return []
#        BFSQ = []
#        res = []
#        rowTmp = []
#        nextStart = 0
#        cursor = 0
#        #start
#        BFSQ.append(root)
#        nextStart = len(BFSQ)
#        while cursor < len(BFSQ):
#            if cursor == nextStart:
#                res.insert(0,list(rowTmp))
#                rowTmp = []
#                nextStart = len(BFSQ)
#            node = BFSQ[cursor]
#            rowTmp.append(node.val)
#            if node.left != None:
#                BFSQ.append(node.left)
#            if node.right != None:
#                BFSQ.append(node.right)
#            cursor += 1
#        res.insert(0,list(rowTmp))
#        return res
#    def zigzagLevelOrder(self, root):
#        if root == None:
#            return []
#        BFSQ = []
#        res = []
#        rowTmp = []
#        orderFlag = True
#        BFSQ.append(root)
#        nextStart = len(BFSQ)
#        cursor = 0
#        while cursor < len(BFSQ):
#            if cursor == nextStart:
#                if orderFlag:
#                    res.append(list(rowTmp))
#                else:
#                    rowTmp.reverse()
#                    res.append(list(rowTmp))
#                rowTmp = []
#                nextStart = len(BFSQ)
#                orderFlag = not orderFlag
#            node = BFSQ[cursor]
#            rowTmp.append(node.val)
#            if node.left != None:
#                BFSQ.append(node.left)
#            if node.right != None:
#                BFSQ.append(node.right)
#            cursor += 1
#        if orderFlag:
#            res.append(list(rowTmp))
#        else:
#            rowTmp.reverse()
#            res.append(list(rowTmp))
#        return res
#    def ladderLength(self, beginWord, endWord, wordDict):
#        dictLen = len(wordDict)
#        wordLen = len(beginWord)
#        if wordLen == 0 or dictLen == 0:
#            return 0
#        if beginWord == endWord or self.oneDiff(beginWord,endWord,wordLen):
#            return 2
#        BFSQ = []
#        record = []
#        cursor = 0
#        while cursor < dictLen:
#            if self.oneDiff(beginWord,wordDict[cursor],wordLen):
#                BFSQ.append(wordDict[cursor])
#                record.append(True)
#            else:
#                record.append(False)
#            cursor += 1
#        cursor = 0
#        res = 3
#        nextStart = len(BFSQ)
#        getFlag = False
#        while cursor < len(BFSQ):
#            if cursor == nextStart:
#                res += 1
#                nextStart = len(BFSQ)
#            newWord = BFSQ[cursor]
#            if self.oneDiff(newWord,endWord,wordLen):
#                getFlag = True
#                break
#            else:
#                tmpCur = 0
#                while tmpCur < dictLen:
#                    if record[tmpCur] == False and self.oneDiff(newWord,wordDict[tmpCur],wordLen):
#                        BFSQ.append(wordDict[tmpCur])
#                        record[tmpCur] = True
#                    tmpCur += 1
#            cursor += 1
#        cursor = 0
#        if getFlag:
#            return res
#        else:
#            return 0
#
#    def oneDiff(self,string1,string2, leng):
#        cursor = 0
#        flag = False
#        while cursor < leng:
#            if string1[cursor] != string2[cursor]:
#                if flag == False:
#                    flag = True
#                else:
#                    flag = False
#                    break
#            cursor += 1
#        return flag
#    def ladderLength2(self,beginWord,endWord,wordDict):
#        dictLen = len(wordDict)
#        wordLen = len(beginWord)
#        if wordLen == 0 or dictLen == 0:
#            return 0
#        if beginWord == endWord or self.oneDiff(beginWord,endWord,wordLen):
#            return 2
#        #begin
#        BFSS = []
#        wordDict = set(wordDict)
#        for candi in wordDict:
#            if self.oneDiff(beginWord,candi,wordLen):
#                BFSS.append(candi)
#        wordDict = wordDict.difference(BFSS)
#        res = 3
#        storeBFSS = []
#        while len(BFSS) > 0:
#            print "BFSS: %d" %len(BFSS)
#            print "Dict: %d" %len(wordDict)
#            for varBFSS in BFSS:
#                #print endWord
#                if self.oneDiff(varBFSS,endWord,wordLen):
#                    return res
#                else:
#                    for candi in wordDict:
#                        if self.oneDiff(varBFSS,candi,wordLen):
#                            storeBFSS.append(candi)
#                    wordDict = wordDict.difference(storeBFSS)
#            #print "dict: %d" %len(wordDict)
#            res += 1
#            tmp = BFSS
#            BFSS = storeBFSS
#            storeBFSS = tmp
#            #print "next BFSS: %d" %len(storeBFSS)
#            storeBFSS = []
#        return 0
#    def ladderLength3(self,beginWord,endWord,wordDict):
#        #pdb.set_trace()
#        wordLen = len(beginWord)
#        dictLen = len(wordDict)
#        if wordLen == 0 or dictLen == 0:
#            return 2
#        wordDict = set(wordDict)
#        res = 2
#        BFSQ = [beginWord]
#        nextRow = []
#        while len(BFSQ) != 0:
#            for node in BFSQ:
#                for i in range(wordLen):
#                    part1 = node[:i]
#                    part2 = node[i+1:]
#                    for mid in "qwertyuiopasdfghjklzxcvbnm":
#                        newWord = part1+mid+part2
#                        if newWord == endWord:
#                            return res
#                        elif newWord in wordDict:
#                            nextRow.append(newWord)
#                            wordDict.remove(newWord)
#            res += 1
#            tmp = BFSQ
#            BFSQ = nextRow
#            nextRow = tmp = []
#        return 0
#    def rightSideView(self, root):
#        if root == None:
#            return None
#        res = []
#        nextRow = []
#        BFSQ = []
#        BFSQ.append(root)
#        while len(BFSQ) > 0:
#            for ind, node in enumerate(BFSQ):
#                if node.left != None:
#                    nextRow.append(node.left)
#                if node.right != None:
#                    nextRow.append(node.right)
#                if ind == len(BFSQ) - 1:
#                    res.append(node.val)
#            tmp = BFSQ
#            BFSQ = nextRow
#            nextRow = tmp = []
#        return res
#    def solve(self, board):
#        if board == []:
#            return []
#        #store '0'
#        maxX = len(board) - 1
#        maxY = len(board[0]) - 1
#        mapSet = set()
#        triggerQ = set()
#        for x, row in enumerate(board):
#            for y, char in enumerate(row):
#                if char == 'O':
#                    mapSet.add((x, y))
#                    if x == maxX or x == 0 or y == maxY or y == 0:
#                        triggerQ.add((x,y))
#        print maxX
#        print maxY
#        print triggerQ
#        print mapSet
#        while len(triggerQ) > 0:
#            BFSQ = []
#            BFSQ.append(triggerQ.pop())
#            while len(BFSQ) > 0:
#                node = BFSQ.pop()
#                print mapSet
#                if (node[0], node[1]) in mapSet:
#                    mapSet.remove((node[0], node[1]))
#                if (node[0] + 1, node[1]) in mapSet:
#                    BFSQ.append((node[0] + 1, node[1]))
#                    mapSet.remove((node[0] + 1, node[1]))
#                if (node[0] - 1, node[1]) in mapSet:
#                    BFSQ.append((node[0] - 1, node[1]))
#                    mapSet.remove((node[0] - 1, node[1]))
#                if (node[0], node[1] - 1) in mapSet:
#                    BFSQ.append((node[0], node[1] - 1))
#                    mapSet.remove((node[0], node[1] - 1))
#                if (node[0], node[1] + 1) in mapSet:
#                    BFSQ.append((node[0], node[1] + 1))
#                    mapSet.remove((node[0], node[1] + 1))
#            triggerQ = mapSet & triggerQ
#        for node in mapSet:
#            oldS = board[node[0]]
#            newS = oldS[:node[1]] + 'X' + oldS[node[1] + 1:]
#            board[node[0]] = newS
#        return board
#    def numIslands(self, grid):
#        if len(grid) == 0:
#            return 0
#        mapSet = set()
#        for x, row in enumerate(grid):
#            for y, val in enumerate(row):
#                print val
#                if val == '1':
#                    mapSet.add((x, y))
#        print mapSet
#        #BFS
#        res = 0
#        while len(mapSet) > 0:
#            res += 1
#            BFS = [mapSet.pop()]
#            while len(BFS) > 0:
#                node = BFS.pop()
#                if node in mapSet:
#                    mapSet.remove(node)
#                if (node[0] + 1,node[1]) in mapSet:
#                    mapSet.remove((node[0] + 1, node[1]))
#                    BFS.append((node[0] + 1, node[1]))
#                if (node[0] - 1,node[1]) in mapSet:
#                    mapSet.remove((node[0] - 1, node[1]))
#                    BFS.append((node[0] - 1, node[1]))
#                if (node[0],node[1] + 1) in mapSet:
#                    mapSet.remove((node[0], node[1] + 1))
#                    BFS.append((node[0], node[1] + 1))
#                if (node[0],node[1] - 1) in mapSet:
#                    mapSet.remove((node[0], node[1] - 1))
#                    BFS.append((node[0], node[1] - 1))
#        return res
#    def preorderTraversal(self, root):
#        res = []
#        if root == None:
#            return res
#        record = set()
#        DFSstack = []
#        DFSstack.append(root)
#        res.append(root.val)
#        record.add(root)
#        #DFS
#        while len(DFSstack) > 0:
#            node = DFSstack[-1]
#            if node.left != None and not node.left in record:
#                DFSstack.append(node.left)
#                res.append(node.left.val)
#                record.add(node.left)
#            elif node.right != None and not node.right in record:
#                DFSstack.append(node.right)
#                res.append(node.right.val)
#                record.add(node.right)
#            else:
#                DFSstack.pop()
#        return res
#    def inorderTraversal(self, root):
#        if root == None:
#            return []
#        record = set()
#        resrec = set()
#        res = []
#        DFSstack =[root]
#        while len(DFSstack) > 0:
#            node = DFSstack[-1]
#            if node.left != None and not node.left in record:
#                DFSstack.append(node.left)
#                record.add(node.left)
#            elif not node in resrec:
#                res.append(node.val)
#                resrec.add(node)
#                if node.right !=None and not node.right in record:
#                    DFSstack.append(node.right)
#                    record.add(node.right)
#            else:
#                DFSstack.pop()
#        return res
#    def flatten(self, root):
#        #put right to left, attach left to rightmost of 1st left node
#        cur = root
#        while cur != None:
#            if cur.left == None:
#                cur = cur.right
#            else:
#                tmp = cur.left
#                while tmp.right != None:
#                    tmp = tmp.right
#                tmp.right = cur.right
#                cur.right = cur.left
#                cur.left = None
#                cur = cur.right
#        cur = root
#        while cur.right != None:
#            print cur.val
#            cur = cur.right
#        print cur.val
#    def sumNumbers(self, root):
#        self.res = 0
#        self.DFSsumNumber(root,0)
#        return self.res
#    def DFSsumNumber(self, root, pre):
#        if root.right == None and root.left == None:
#            self.res += 10 * pre + root.val
#        else:
#            self.DFSsumNumber(root.left, pre * 10 + root.val)
#            self.DFSsumNumber(root.right, pre * 10 + root.val)
#    def sumNumbersNoRecur(self, root):
#        res = 0
#        DFSstack = []
#        node = root
#        valStack = []
#        tmp = 0
#        #pdb.set_trace()
#        while node != None:
#            tmp = tmp * 10 + node.val
#            if node.left != None:
#                if node.right != None:
#                    DFSstack.append(node.right)
#                    valStack.append(tmp)
#                node = node.left
#            else:
#                if node.right != None:
#                    node = node.right
#                else:
#                    res += tmp
#                    if len(DFSstack) != 0:
#                        node = DFSstack.pop()
#                        tmp = valStack.pop()
#                    else:
#                        node = None
#        return res
#    def pathSum(self, root, sum):
#        #stack DFS
#        DFSstack = []
#        node = root
#        #Q related
#        tmp = []
#        res = []
#        val = []
#        tmpStack = []
#        pre = 0
#        while node != None:
#            pre += node.val
#            tmp.append(node.val)
#            if node.left != None:
#                if node.right != None:
#                    DFSstack.append(node.right)
#                    val.append(pre)
#                    tmpStack.append(list(tmp))
#                node = node.left
#            else:
#                if node.right != None:
#                    node = node.right
#                else:
#                    #cal tmp
#                    if pre == sum:
#                        res.append(list(tmp))
#                    if len(DFSstack) != 0:
#                        node = DFSstack.pop()
#                        pre = val.pop()
#                        tmp = tmpStack.pop()
#                    else:
#                        node = None
#        return res
#    def sortedListToBST(self, head):
#        if head != None:
#            midPre = self.__getMidPre(head)
#            mid = midPre.next
#            midPre.next = None
#            if mid == None:
#                #only one member
#                return myBTree.myBTree.myBTree.TreeNode(midPre.val)
#            else:
#                root = myBTree.myBTree.myBTree.TreeNode(mid.val)
#                self.__buildBST(root, head, mid.next)
#                return root
#        else:
#            return None
#    def __buildBST(self, p, h1, h2):
#        if h1 != None:
#            midPre = self.__getMidPre(h1)
#            mid = midPre.next
#            midPre.next = None
#            if mid == None:
#                #only one node
#                p.left = myBTree.myBTree.myBTree.TreeNode(midPre.val)
#            else:
#                p.left = myBTree.myBTree.myBTree.TreeNode(mid.val)
#                self.__buildBST(p.left, h1, mid.next)
#        if h2 != None:
#            midPre = self.__getMidPre(h2)
#            mid = midPre.next
#            midPre.next = None
#            if mid == None:
#                #only one node
#                p.right = myBTree.myBTree.myBTree.TreeNode(midPre.val)
#            else:
#                p.right = myBTree.myBTree.myBTree.TreeNode(mid.val)
#                self.__buildBST(p.right, h2, mid.next)
#
#    def __getMidPre(self, head):
#        i = 1
#        mid = self.__getLen(head) / 2
#        while i < mid:
#            head = head.next
#            i += 1
#        return head
#    def __getLen(self, head):
#        res = 0
#        while head != None:
#            head = head.next
#            res += 1
#        return res
#    def sortedListToBST2(self, head):
#        #to sorted ary
#        sortAry = []
#        while head != None:
#            sortAry.append(head.val)
#            head = head.next
#        #sorted ary to BST
#        midID = (len(sortAry) - 1) / 2
#        root = myBTree.myBTree.TreeNode(sortAry[midID])
#        self.__buildBST2(root, sortAry, 0, len(sortAry) - 1)
#        return root
#
#    def __buildBST2(self, root, ary, id1, id2):
#        if id1 == id2:
#            return
#        elif id1 == id2 - 1:
#            root.right = myBTree.myBTree.TreeNode(ary[id2])
#        else:
#            rootID = (id2 + id1) / 2
#            leftID = (id1 + rootID -1) / 2
#            rightID = (id2 + rootID + 1) / 2
#            root.left = myBTree.myBTree.TreeNode(ary[leftID])
#            root.right = myBTree.myBTree.TreeNode(ary[rightID])
#            self.__buildBST2(root.left, ary, id1, rootID - 1)
#            self.__buildBST2(root.right, ary, rootID + 1, id2)
#    def buildTree(self, preorder, inorder):
#        #return self.__buildBST(0, preorder, inorder)
#        #return self.__buildBST3(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
#        self.__buildBST4(postorder, inorder, 0, len(postorder) - 1, 0, len(inorder) - 1)
#    def __buildBST(self, pid, pre, ino):
#        if len(ino) == 0:
#            return None
#        rVal = pre[pid]
#        node = myBTree.TreeNode(rVal)
#        inRid = ino.index(rVal)
#        subLeft = ino[:inRid]
#        subRight = ino[inRid + 1:]
#        node.left = self.__buildBST(pid + 1, pre, subLeft)
#        node.right = self.__buildBST(pid + inRid + 1, pre, subRight)
#        return node
#    def __buildBST3(self, pre, i, j, ino, ii, jj):
#        '''preorder and inorder build BST: good!!!!!!!'''
#        if i > j or ii > jj:
#            return None
#        else:
#            rVal = pre[i]
#            node = myBTree.TreeNode(rVal)
#            inID = ino.index(rVal)
#            dis = inID - ii
#            node.left = self.__buildBST3(pre, i + 1, i + dis, ino, ii, inID - 1)
#            node.right = self.__buildBST3(pre, dis + i + 1, j, ino, inID + 1, jj)
#            return node
#    def __buildBST4(self, post, ino, i, j, ii, jj):
#        '''postorder and inorder build BST'''
#        if j < i or jj < ii:
#            return None
#        rVal = post[j]
#        inID = ino.index(rVal)
#        node = myBTree.TreeNode(rVal)
#        dis = jj - inID
#        node.right = self.__buildBST4(post, ino, j - dis, j - 1, inID + 1, jj)
#        node.left = self.__buildBST4(post, ino, i, j - dis - 1, ii, inID -1)
#        return node

