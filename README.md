# Python

## Data

### data type

`Boolean`, `Int`, `Long`, `Float`

### Data Structure

#### Basic DS:

* `[]`, `{}`, `()`, `set([])`

*  [reference](https://docs.python.org/2/tutorial/datastructures.html#)

#### Import collections:

* `deque`, `Counter`, `OrderedDict`, `defaultdict`, `namedtuple`

* [reference](https://docs.python.org/2/library/collections.html#collections.OrderedDict)

#### Higher level:

* `heapq`, `Queue`

#### Need Implement:

* `Trie`

#### Article:

[1] [basic](http://code.tutsplus.com/articles/advanced-python-data-structures--net-32748)

[2] [basic & import](http://www.informit.com/articles/article.aspx?p=1719315)

[3] [heapq](http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php)

### Implement

####Heap


####Trie


## Coding

### Pythonic

```py
#empty string can use not a
a = ""
if not a:
	#run /w empty a
```

```py
#Created object can have dynamic attributes, built-in DS cannot
class Object(object):
	pass
aa = Object
aa.flag = True #add flag dynamically
if hasattr(aa,'flag'):
	print aa.flag #print True

bb = {}
try:
	bb.flag = True
except Exception, e:
	print e #'dict' object has no attribute 'flag'
```

```py

```

### Higher Performance

#### String Related

```py
# use join instead of +=
a = ["as", "you", "sunny"]
res = " ".join(a)

#print
a = {'a': 1, 'b':2}
res = "hello %(a)s and %(b)s" %a
```

#### Loop Related

```py
# map > local & dot > basic
# map(func, iter) call func for every iter, not good for overlap operation
# record .func as lcoal variable
# use xrange() instead of range()
oldlist = "asdfs"
newlist = []
newlist = map(str.upper, oldlist)

upper = str.upper
append = newlist.append()
for var in oldlist:
    append(upper(var))
```

#### Dictionary

```py
# try is better than if
# use .get(index, 0)
# use collections.defaultdict
```

#### Calculate

```py
# + > >> or << > * or /

```

#### Profiling

```py
# several module
```

### Memory access

#### Touch **address**

```py
# id()

# iterator
a = [1,2,3,4]
b = iter(a)
print next(b)
```

### Tricks

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
