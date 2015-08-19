import pdb 

class Solution:
    def isHappy(self, n):
        res = n
        dupDic = set([])
        while True:
            if res == 1:
                return True
            elif res in dupDic:
                return False
            else:
                dupDic.add(res)
            lef = res
            res = 0
            while lef != 0:
                cal = lef % 10
                res += pow(cal ,2)
                lef /= 10
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if not s:
            return True
        tl = len(s)
        i = 0
        rec = {}
        while i < tl:
            if s[i] != t[i]:
                if s[i] in rec:
                    rec[s[i]] += 1
                else:
                    rec[s[i]] = 1
                if t[i] in rec:
                    rec[t[i]] -= 1
                else:
                    rec[t[i]] = -1
            i += 1
        for key in rec:
            if rec[key] != 0:
                return False
        return True
