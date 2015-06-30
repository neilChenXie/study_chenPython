#!/usr/bin/python

class Person:
    populate = 0
    def __init__(self,name):
        self.name = name
        Person.populate += 1

    def __del__(self):
        Person.populate -= 1
        print '%s is leaving' % self.name
        if Person.populate == 0:
            print 'the house is empty'
    
    def sayHi(self):
        print '%s: hello world, I\'m the %d th person' % (self.name, Person.populate)
    
    def sayAgain(self):
        print '%s: see you sayAgain. %d people remained' % (self.name, Person.populate)



p1 = Person("chen")
p1.sayHi()
p2 = Person('xie')
p2.sayHi()
p3 = Person('yuan')
p3.sayHi()

#p1.sayAgain()
p3.sayAgain()
