# Python

## Data

* data type

* data Structure

    * basic: Boolean, Int, Long, Float

    * basic DS: `[]`, `{}`, `()`, `set([])`

        * [Reference](https://docs.python.org/2/tutorial/datastructures.html#)

    * import collections: `deque`, `Counter`, `OrderedDict`

        * [Reference](https://docs.python.org/2/library/collections.html#collections.OrderedDict)

  * higher level:

## Coding

* Pythonic

* Higher Performance

    * iterator
        ```py
        a = [1,2,3,4]
        itor = iter(a)
        print next(itor) #print 1
        for i in itor:
            #skipped the 1st element
        ```

* Lower level access

    * get object or variable **address**

        * id()

* Tricks
    * x = a or b
        ```py
        #one of a,b is equal to None
        if a or b:
            x = a or b
        ```

    * `hasattr()` check whether it has additional attributes
        ```py
        while newHead != None:
            if hasattr(newHead,'flag') and newHead.flag == True:
                return newHead
                newHead.flag = True
            return None
        ```

    * `print`

        * without newline
            ```py
            #the last , is indicate
            print str(node.value) , "->" ,
            ```

        * any format
            ```py
            a = [1,2,3]
            print "the list:%r" %a
            ```




## Structure & Design Skill

* OOP

  * class variable & object variable

  * no virtual function like C++

  * don't touch member directly

* Structure

  * multi-file use **os** and **sys** module to change `path`

  * module
      * `__name__`: `__main__` or `module`


## Fault List

* `and` instead of `&&`

* create **intersection** link list

    > cannot append multiple nodes one by one to 2 link lists, because when we append them to the 1st list, all nodes are linked together, for the 2nd list, there will be circle.

* file name cannot be `string.py`

## Reference

[1] [Pythonic](https://www.python.org/dev/peps/pep-0008/#indentation)
[2] [Improve Performance](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
[3] [Except System](https://docs.python.org/2/tutorial/errors.html)
