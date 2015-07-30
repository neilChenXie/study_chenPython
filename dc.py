import pdb
import re

class Solution:
    def majorityElement(self, nums):
        #hashtable
        i = 0
        counter = {}
        leng = len(nums)
        while i < leng:
            mapKey = nums[i]
            if mapKey not in counter:
                counter[mapKey] = 1
                i += 1
                continue
            else:
                counter[mapKey] += 1
                if counter(mapKey) > leng / 2:
                    return mapKey
    def searchMatrix(self, matrix, target):
        return self.__doSq(matrix, 0, len(matrix[0]) - 1, target)

    def __doSq(self, matrix, x, y, target):
        print "x:%d, y:%d" %(x,y)
        if y < 0:
            return False
        while x < len(matrix):
            if matrix[x][0] > target or matrix[x][y] < target:
                x += 1
            else:
                break
        if x == len(matrix):
            return False
        #do BS
        h = 0
        t = y
        while h <= t:
            tmp = (h + t) / 2
            if matrix[x][tmp] < target:
                h = tmp + 1
            elif matrix[x][tmp] > target:
                t = tmp -1
            else:
                return True
        return self.__doSq(matrix, x + 1, h - 1, target)
    def __add(v1,v2):
        return v1 + v2
    def __min(v1,v2):
        return v1 - v2
    def __mul(v1, v2):
        return v1 * v2
    opt = {
        '+':__add,
        '-':__min,
        '*':__mul
    }
    def diffWaysToCompute(self, input):
        self.numAry = re.split("[*+-]",input)
        self.optAry = re.split('\d',input)
        self.optAry = filter(None, self.optAry)
        return self.__doCal(0, len(self.numAry) -1)
    def __doCal(self, h, t):
        print "h:%d, t:%d" %(h,t)
        if h == t:
            rv = int(self.numAry[h])
            return [rv]
        if h + 1 == t:
            rv = self.opt[self.optAry[h]](int(self.numAry[h]), int(self.numAry[t]))
            return [rv]
        else:
            tmp = []
            i = h
            while i < t:
                op = self.optAry[i]
                for v1 in self.__doCal(h,i):
                    for v2 in self.__doCal(i+1,t):
                        tmp.append(self.opt[op](v1,v2))
                i += 1
        return tmp
