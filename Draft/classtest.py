#!/usr/bin/python

class Swit:
    def __init__(self):
        print "start"

    def printHello():
        print "hello world"

    pc = {'a':printHello,
    }

    def usePc(self):
        self.pc['a']()


aa = Swit()
aa.usePc()
