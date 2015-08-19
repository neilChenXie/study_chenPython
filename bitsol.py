import pdb

class Solution:
    def rangeBitwiseAnd(self, m, n):
        res = m
        for i in range(m, n + 1):
            res &= i
        return res
    def hammingWeight(self, n):
        endSign = 1
        endTar = n
        move = 1
        res = 0
        while True:
            if endSign > endTar:
                break
            endSign = endSign << 1
            if n & 1 == 1:
                res += 1
            n = n >> move
        return res

