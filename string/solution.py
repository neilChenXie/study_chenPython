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
