class DLinkNode:
    def __init__(self, value = None):
        self.val = value
        self.pre = None
        self.nex = None
class DLink:
    def __init__(self):
        self.root = DLinkNode()
        self.root.nex = self.root
        self.root.pre = self.root
        self.leng = 0
    def insert(self, val):
        node = DLinkNode(val)
        node.nex = self.root.nex
        node.pre = self.root
        self.root.nex.pre = node
        self.root.nex = node
        if self.leng == 0:
            self.root.pre = node
        self.leng += 1
        return node
    def pop(self):
        if self.leng == 0:
            return None
        self.leng -= 1
        p = self.root.pre
        self.root.pre = p.pre
        p.pre.nex = self.root
        return p.val
    def getLast(self):
        if self.leng == 0:
            return None
        else:
            return self.root.pre.val
    def getLen(self):
        return self.leng
    def lruUpdate(self, node, val):
        node.val = val
        node.pre.nex = node.nex
        node.nex.pre = node.pre
        node.nex = self.root.nex
        node.pre = self.root
        self.root.nex.pre = node
        self.root.nex = node
    def lruGet(self, node):
        node.pre.nex = node.nex
        node.nex.pre = node.pre
        node.pre = self.root
        node.nex = self.root.nex
        self.root.nex.pre = node
        self.root.nex = node
        return node.val
    def printList(self):
        p = self.root.nex
        while p != self.root:
            print p.val
            p = p.nex

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}
        self.dlist = DLink()
        self.capacity = capacity
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.table:
            #update position
            rv = self.dlist.lruGet(self.table[key])
            # self.dlist.printList()
            return rv[1]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.table:
            rv = self.dlist.insert((key, value))
            self.table[key] = rv
            # self.dlist.printList()
            if self.dlist.getLen() > self.capacity:
                # need to remove the last
                rm = self.dlist.pop()
                del self.table[rm[0]]
                # self.dlist.printList()
        else:
            # already in table
            self.dlist.lruUpdate(self.table[key], (key, value))
        # self.dlist.printList()
