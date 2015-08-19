import pdb

class Solution:
    def solveNQueens(self, n):
        colRec = [0 for y in range(n)]
        rc = [0 for x in range(2*n - 1)]
        cr = [0 for x in range(2*n - 1)]
        #tmpRes = [-1 for x in range(n)]
        #self.res = []
        self.count = 0
        #self.__doQueen(colRec, rc, cr, 0, tmpRes)
        self.__doQueenCount(colRec, rc, cr, 0)
        #return self.res
    def __doQueenCount(self, colRec, rc, cr, rowN):
        if rowN == len(colRec):
            #change tmpRes to output
            self.count += 1
            return
        #scan all possible col
        for col in range(len(colRec)):
            if colRec[col] == 0 and rc[rowN - col + len(colRec) - 1] == 0 and cr[col + rowN] == 0:
                colRec[col], rc[rowN - col + len(colRec) - 1], cr[col + rowN] = 1, 1, 1
                self.__doQueen(colRec, rc, cr, rowN + 1)
                colRec[col], rc[rowN - col + len(colRec) - 1], cr[col + rowN] = 0, 0, 0
        return
        
    def __doQueen(self, colRec, rc, cr, rowN, tmpRes):
        if rowN == len(colRec):
            #change tmpRes to output
            self.__queenOut(tmpRes)
            return
        #scan all possible col
        for col in range(len(colRec)):
            if colRec[col] == 0 and rc[rowN - col + len(colRec) - 1] == 0 and cr[col + rowN] == 0:
                tmpRes[rowN] = col
                colRec[col], rc[rowN - col + len(colRec) - 1], cr[col + rowN] = 1, 1, 1
                self.__doQueen(colRec, rc, cr, rowN + 1, tmpRes)
                tmpRes[rowN] = -1
                colRec[col], rc[rowN - col + len(colRec) - 1], cr[col + rowN] = 0, 0, 0
        return
    def __queenOut(self, res):
        sol = []
        n = len(res)
        for var in res:
            tmp = '.' * var + 'Q' + '.' * (n - var - 1)
            sol.append(tmp)
        self.res.append(sol)

#    def partition(self, s):
#        self.res = []
#        self.__doCheck(s, 0, [])
#        return self.res
#    def __doCheck(self, s, h, tmp):
#        if h == len(s):
#            self.res.append(list(tmp))
#            return
#        tmp.append(s[h:h+1])
#        self.__doCheck(s, h + 1, tmp)
#        tmp.pop()
#        i = 2
#        while h + i <= len(s):
#            if self.__checkPalind(s, h, h + i - 1):
#                tmp.append(s[h:h+i])
#                self.__doCheck(s, h + i, tmp)
#                tmp.pop()
#            i += 1
#    def __checkPalind(self, s, h, t):
#        while h < t:
#            if s[h] != s[t]:
#                return False
#            h += 1
#            t -= 1
#        return True
#    def grayCode(self, n):
#        '''gray code seq'''
#        res = [0]
#        for i in range(n):
#            res += [pow(2, i) + x for x in reversed(res)]
#        return res
#    def restoreIpAddresses(self, s):
#        '''get all possible IP address'''
#        self.res = []
#        tmpRes = ""
#        self.__oneIP(s, 0, 0, tmpRes)
#        return self.res
#    def __oneIP(self,s, h, i, tmpRes):
#        if h >= len(s):
#            return
#        elif i == 3:
#            deci = int(s[h:])
#            if (len(s) - h == 3 and deci > 100 and deci <= 255) or (len(s) - h == 2 and deci >= 10) or len(s) - h == 1:
#                tmpRes += s[h:]
#                self.res.append(tmpRes)
#            return
#        else:
#            if h + 1 < len(s):
#                self.__oneIP(s, h+1, i + 1, tmpRes + s[h:h+1] + ".") 
#            if h + 2 < len(s) and int(s[h:h+2]) >= 10:
#                self.__oneIP(s, h+2, i + 1, tmpRes + s[h:h+2] + ".") 
#            #when tmp  = 3
#            if h + 3 < len(s) and int(s[h:h+3]) <= 255 and int(s[h:h+3]) >= 100:
#                self.__oneIP(s, h+3, i + 1, tmpRes + s[h:h+3] + ".") 
#            return


                
