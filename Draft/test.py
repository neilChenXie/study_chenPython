#!/usr/bin/python

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print self.name + ' hello world'


p = Person("chen")
p.sayHi()
