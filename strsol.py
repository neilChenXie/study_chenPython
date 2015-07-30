import pdb

class Solution:
    def simplifyPath(self, path):
        res = []
        subPath = path.split("/")
        print subPath
        if subPath[0] == '':
            res.append('/')
        for var in subPath[1:]:
            if var == '..':
                if len(res) != 0 and res[-1] != '/':
                    res.pop()
            elif var != '' and var != '.':
                res.append(var)
        #construct output
        print res
        rv = str()
        for var in res:
            if var == '/':
                rv = rv + var
            elif var != res[-1]:
                rv = rv + var + '/'
            else:
                rv = rv + var
        return rv
    def evalRPN(self, tokens):
        cont = []
        for var in tokens:
            if var in "+-*/":
                two = cont.pop()
                one = cont.pop()
                if var == "+":
                    cont.append(one + two)
                elif var == '-':
                    cont.append(one - two)
                elif var == '*':
                    cont.append(one * two)
                else:
                    addFlag = one % two
                    if addFlag != 0:
                        cont.append((one / two) + 1)
                    else:
                        cont.append(one / two)
            else:
                cont.append(int(var))
            print cont
        return cont.pop()
    def calculate(self, s):
        #always valid expression
        intStore = 0
        calStack = []
        for var in s:
            #pdb.set_trace()
            if var == ')':
                # finish of intStore
                if intStore != 0:
                    calStack.append(intStore)
                    intStore = 0
                #cal to last '('
                while True:
                    calM1 = calStack.pop()
                    opt = calStack.pop()
                    if opt == "(":
                        calStack.append(calM1)
                        break
                    calM2 = calStack.pop()
                    if opt == "+":
                        calStack.append(calM2 + calM1)
                    else:
                        calStack.append(calM2 - calM1)
            elif var == '(':
                calStack.append(var)
            elif var in "+-":
                #end of intStore, append
                if intStore != 0:
                    calStack.append(intStore)
                    intStore = 0
                if len(calStack) > 1 and calStack[-2] != '(':
                    calM1 = calStack.pop()
                    opt = calStack.pop()
                    calM2 = calStack.pop()
                    if opt == "+":
                        calStack.append(calM1 + calM2)
                    else:
                        calStack.append(calM2 - calM1)
                calStack.append(var)
            else:
                #integer
                intStore = 10 * intStore + int(var)
        while len(calStack) >= 3:
            calM1 = calStack.pop()
            opt = calStack.pop()
            calM2 = calStack.pop()
            if opt == "+":
                calStack.append(calM1 + calM2)
            else:
                calStack.append(calM2 - calM1)
        return calStack[0]

    def __one(res):
        if len(res) == 0:
            for addTo in "abc":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "abc":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __two(res):
        if len(res) == 0:
            for addTo in "def":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "def":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __three(res):
        if len(res) == 0:
            for addTo in "ghi":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "ghi":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __four(res):
        if len(res) == 0:
            for addTo in "jkl":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "jkl":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __five(res):
        if len(res) == 0:
            for addTo in "mno":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "mno":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __six(res):
        if len(res) == 0:
            for addTo in "pqrs":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "pqrs":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __seven(res):
        if len(res) == 0:
            for addTo in "tuv":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "tuv":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp
    def __eight(res):
        if len(res) == 0:
            for addTo in "wxyz":
                res.append(addTo)
            return res
        tmp = []
        for addTo in "wxyz":
            i = 0
            while i < len(res):
                tmp.append(res[i] + addTo)
                i += 1
        return tmp

    option = {"2":__one,
              "3":__two,
              "4":__three,
              "5":__four,
              "6":__five,
              "7":__six,
              "8":__seven,
              "9":__eight,
    }

    def letterCombinations(self, digits):
        if digits == None or digits == "":
            return None
        res = []
        for var in digits:
            res = self.option[var](res)
        return res
    def longestValidParentheses(self, s):
        tmp = 0
        res = 0
        stack = []
        flag = True
        pre = 0
        #pdb.set_trace()
        for (i, var) in enumerate(s):
            if var == '(':
                stack.append(i)
            elif var == ')':
                if len(stack) != 0:
                    tmp = i - stack.pop() + 1
                    if len(stack) == 0:
                        if flag:
                            tmp += pre
                        flag = True
                    res = max(res, tmp)
                    pre = tmp
            else:
                flag = False
        return res
