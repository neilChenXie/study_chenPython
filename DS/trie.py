class pyTrie:
    def __init__():
        self.root = {}
    def addWord(self, word):
        p = self.root
        for var in word:
             p = p.setdefault(var,{})
        p[None] = None
    def search(self, word):
        p = self.root
        for var in word:
            if var in p:
                p = p[var]
            else:
                return False
        return None in p
                
class TrieNode:
    def __init__(self):
        self.val = False
        self.next = [None for i in xrange(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        p = self.root
        for char in word:
            asc = ord(char) - ord('a')
            if p.next[asc] == None:
                p.next[asc] = TrieNode()
            p = p.next[asc]
        p.val = True

    def search(self, word):
        p = self.root
        for char in word:
            asc = ord(char) - ord('a')
            if p.next[asc] == None:
                return False
            else:
                p = p.next[asc]
        if p.val:
            return True
        else:
            return False

    def startsWith(self, prefix):
        p = self.root
        for char in prefix:
            asc = ord(char) - ord('a')
            if p.next[asc] == None:
                return False
            p = p.next[asc]
        return True

class WordDictionary():
    def __init__(self):
        self.root = {}
    def addWord(self, word):
        p = self.root
        for var in word:
            if var not in p:
                p.setdefault(var,{})
            p = p[var]
        p[None] = None
    def search(self, word):
        return self.__trieSearch(self.root, word, 0)
    def __trieSearch(self, node, word, i):
        if not node:
            return False
        elif i == len(word):
            return True
        elif word[i] != ".":
            return word[i] in node and self.__trieSearch(node[word[i]], word, i + 1)
        else:
            return any(self.__trieSearch(node[ind], word, i + 1) for ind in node)
        
