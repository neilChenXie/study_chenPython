#!/usr/bin/python

class Solution:
    def numTrees(self, n):
        return self.__doCal(n,[])
        
    def __doCal(self,n, tmp):
        if n < len(tmp):
            return tmp[n]
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            res = 0
            for i in range(n):
                res += self.__doCal(i,tmp) + self.__doCal(n - 1 - i, tmp) 
            tmp.append(res)
            return res
#	def minimumTotal(self, triangle):
#		'''find the minimum sum path'''
#		if triangle == [] or triangle == [[]]:
#			return None
#		rowI = len(triangle) - 1
#		while rowI > 0:
#			colJ = 0
#			while colJ < len(triangle[rowI]) - 1:
#				if triangle[rowI][colJ] <= triangle[rowI][colJ + 1]:
#					triangle[rowI - 1][colJ] += triangle[rowI][colJ]
#				else:
#					triangle[rowI - 1][colJ] += triangle[rowI][colJ + 1]
#				colJ += 1
#			rowI -= 1
#		return triangle[0][0]
		
