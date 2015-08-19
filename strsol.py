import pdb

class Solution:
    def numDistinct(self, s, t):
        '''distinct subsequences of T in S, O(n^k)'''
        self.res = 0
        self.__findNext(s, t, 0, 0)
        return self.res
    def __findNext(self, s, t, sh, th):
        if th == len(t):
            self.res += 1
            return
        elif sh == len(s):
            return
        else:
            while sh < len(s):
                ns = sh
                while ns < len(s) and s[ns] != t[th]:
                    ns += 1
                if ns == len(s):
                    return
                else:
                    self.__findNext(s, t, ns + 1, th + 1)
                    sh = ns + 1
            return

#    def compareVersion(self, version1, version2):
#        return self.__doComp(0, 0, version1, version2)
#    def __doComp(self,h1,h2,v1,v2):
#        '''can handle every version situation'''
#        #pdb.set_trace()
#        an1 = h1
#        an2 = h2
#        while h1 < len(v1) and v1[h1] != '.':
#            h1 += 1
#        while h2 < len(v2) and v2[h2] != '.':
#            h2 += 1
#        if int(v1[an1:h1]) > int(v2[an2:h2]):
#            return 1
#        elif int(v1[an1:h1]) < int(v2[an2:h2]):
#            return -1
#        else:
#            if h1 == len(v1) and h2 == len(v2):
#                return 0
#            elif h1 != len(v1) and h2 != len(v2):
#                return self.__doComp(h1 + 1, h2 + 1, v1, v2)
#            elif h1 != len(v1):
#                if self.__equZero(h1 + 1, v1):
#                    return 0
#                return 1
#            else:
#                if self.__equZero(h2 + 1, v2):
#                    return 0
#                return -1
#    def __equZero(self, h, v):
#        an = h
#        while h < len(v) and v[h] != '.':
#            h += 1
#        if int(v[an:h]) == 0:
#            if h == len(v):
#                return True
#            else:
#                return self.__equZero(h + 1,v)
#        else:
#            return False
        

#    def longestPalindrome(self, s):
#        '''expand central'''
#        i = 0
#        rech = 0
#        rect = 0
#        while i < len(s):
#            k,j = i, i
#            while k < len(s) - 1 and s[k + 1] ==s[k]:
#                k += 1
#            i = k
#            while j > 0 and k < len(s) - 1 and s[j - 1] == s[k + 1]:
#                j -= 1
#                k += 1
#            if k - j > rect - rech:
#                rect = k
#                rech = j
#            i += 1
#        return s[rech:rect + 1]
#
#    def reverseWords(self, s):
#        '''use every tools'''
#        s = s.strip()
#        h = 0
#        res = ""
#        while h < len(s):
#            while s[h] == ' ':
#                h += 1
#            t = h
#            while t < len(s) - 1 and s[t + 1] != ' ':
#                t += 1
#            if h == 0:
#                res += s[t::-1]
#            else:
#                res += s[t:h - 1: -1]
#            res += " "
#            h = t + 1
#        return res[-2::-1]
#
#    def reverseWords(self, s):
#        '''without using any method of string'''
#        h = 0
#        t = 0
#        res = ""
#        while h < len(s) and t < len(s):
#            while h < len(s) and s[h] == ' ':
#                h += 1
#            if h == len(s):
#                break
#            t = h 
#            while t < len(s) - 1 and s[t + 1] != ' ':
#                t += 1
#            if h == 0:
#                res += (s[t::-1] + ' ')
#            else:
#                res += (s[t:h - 1:-1] + ' ')
#            h = t + 1
#        return res[len(res) - 2::-1]

#    def addBinary(self, a, b):
#        longStr, shortStr = None, None
#        if len(a) >= len(b):
#            longStr = a[::-1]
#            shortStr = b[::-1]
#        else:
#            longStr = b[::-1]
#            shortStr = a[::-1]
#        res = ""
#        c = False
#        for i in range(len(shortStr)):
#            print res
#            if longStr[i] == shortStr [i] == '0' and not c:
#                res += "0"
#            elif longStr[i] == shortStr[i] == '0' and  c:
#                res += "1"
#                c = False
#            elif longStr[i] == shortStr[i] == '1' and c:
#                res += "1"
#            elif longStr[i] == shortStr[i] == "1" and not c:
#                res += "0"
#                c = True
#            elif c:
#                res += "0"
#            else:
#                res += "1"
#        i += 1
#        if c:
#            while i < len(longStr):
#                if longStr[i] == '0':
#                    c = False
#                    res += "1"
#                    break
#                else:
#                    res += "0"
#                i += 1
#            if c:
#                res += "1"
#        return res[::-1]

#    def simplifyPath(self, path):
#        res = []
#        subPath = path.split("/")
#        print subPath
#        if subPath[0] == '':
#            res.append('/')
#        for var in subPath[1:]:
#            if var == '..':
#                if len(res) != 0 and res[-1] != '/':
#                    res.pop()
#            elif var != '' and var != '.':
#                res.append(var)
#        #construct output
#        print res
#        rv = str()
#        for var in res:
#            if var == '/':
#                rv = rv + var
#            elif var != res[-1]:
#                rv = rv + var + '/'
#            else:
#                rv = rv + var
#        return rv
#    def evalRPN(self, tokens):
#        cont = []
#        for var in tokens:
#            if var in "+-*/":
#                two = cont.pop()
#                one = cont.pop()
#                if var == "+":
#                    cont.append(one + two)
#                elif var == '-':
#                    cont.append(one - two)
#                elif var == '*':
#                    cont.append(one * two)
#                else:
#                    addFlag = one % two
#                    if addFlag != 0:
#                        cont.append((one / two) + 1)
#                    else:
#                        cont.append(one / two)
#            else:
#                cont.append(int(var))
#            print cont
#        return cont.pop()
#    def calculate(self, s):
#        #always valid expression
#        intStore = 0
#        calStack = []
#        for var in s:
#            #pdb.set_trace()
#            if var == ')':
#                # finish of intStore
#                if intStore != 0:
#                    calStack.append(intStore)
#                    intStore = 0
#                #cal to last '('
#                while True:
#                    calM1 = calStack.pop()
#                    opt = calStack.pop()
#                    if opt == "(":
#                        calStack.append(calM1)
#                        break
#                    calM2 = calStack.pop()
#                    if opt == "+":
#                        calStack.append(calM2 + calM1)
#                    else:
#                        calStack.append(calM2 - calM1)
#            elif var == '(':
#                calStack.append(var)
#            elif var in "+-":
#                #end of intStore, append
#                if intStore != 0:
#                    calStack.append(intStore)
#                    intStore = 0
#                if len(calStack) > 1 and calStack[-2] != '(':
#                    calM1 = calStack.pop()
#                    opt = calStack.pop()
#                    calM2 = calStack.pop()
#                    if opt == "+":
#                        calStack.append(calM1 + calM2)
#                    else:
#                        calStack.append(calM2 - calM1)
#                calStack.append(var)
#            else:
#                #integer
#                intStore = 10 * intStore + int(var)
#        while len(calStack) >= 3:
#            calM1 = calStack.pop()
#            opt = calStack.pop()
#            calM2 = calStack.pop()
#            if opt == "+":
#                calStack.append(calM1 + calM2)
#            else:
#                calStack.append(calM2 - calM1)
#        return calStack[0]
#
#    def __one(res):
#        if len(res) == 0:
#            for addTo in "abc":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "abc":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __two(res):
#        if len(res) == 0:
#            for addTo in "def":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "def":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __three(res):
#        if len(res) == 0:
#            for addTo in "ghi":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "ghi":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __four(res):
#        if len(res) == 0:
#            for addTo in "jkl":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "jkl":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __five(res):
#        if len(res) == 0:
#            for addTo in "mno":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "mno":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __six(res):
#        if len(res) == 0:
#            for addTo in "pqrs":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "pqrs":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __seven(res):
#        if len(res) == 0:
#            for addTo in "tuv":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "tuv":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#    def __eight(res):
#        if len(res) == 0:
#            for addTo in "wxyz":
#                res.append(addTo)
#            return res
#        tmp = []
#        for addTo in "wxyz":
#            i = 0
#            while i < len(res):
#                tmp.append(res[i] + addTo)
#                i += 1
#        return tmp
#
#    option = {"2":__one,
#              "3":__two,
#              "4":__three,
#              "5":__four,
#              "6":__five,
#              "7":__six,
#              "8":__seven,
#              "9":__eight,
#    }
#
#    def letterCombinations(self, digits):
#        if digits == None or digits == "":
#            return None
#        res = []
#        for var in digits:
#            res = self.option[var](res)
#        return res
#    def longestValidParentheses(self, s):
#        tmp = 0
#        res = 0
#        stack = []
#        flag = True
#        pre = 0
#        #pdb.set_trace()
#        for (i, var) in enumerate(s):
#            if var == '(':
#                stack.append(i)
#            elif var == ')':
#                if len(stack) != 0:
#                    tmp = i - stack.pop() + 1
#                    if len(stack) == 0:
#                        if flag:
#                            tmp += pre
#                        flag = True
#                    res = max(res, tmp)
#                    pre = tmp
#            else:
#                flag = False
#        return res
