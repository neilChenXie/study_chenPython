#Python

##Fundamental

* `#` for comment
*  `%` for `print`
    * What is the difference between `%r` and `%s` ?
        * Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.
    * What's the point of %s and %d when you can just use %r?
        * The %r is best for debugging, and the other formats are for actually displaying variables to users.
* `[]`, `{}` and `()`

    * `[]`: list

    * `{}`: dictionary

    * `()`: tuple

* module
  * `__name__`: `__main__` or `module`
* get object or variable **address**
  * id()
##Design Skill

* OOP
  * class variable & object variable
  * no virtual function like C++
  * don't touch member directly

* Structure

  * multi-file use **os** and **sys** module to change `path`

##Coding Skill

* x = a or b
```py
#one of a,b is equal to None
if a or b:
	x = a or b
```
* `print` without newline
```py
  print str(node.value) , "->" ,
```
* `hasattr()` check whether it has additional attributes
```py
while newHead != None:
    if hasattr(newHead,'flag') and newHead.flag == True:
        return newHead
    newHead.flag = True
return None
```
##Fault List

* `and` instead of `&&`

* create **intersection** link list

    > cannot append multiple nodes one by one to 2 link lists, because when we append them to the 1st list, all nodes are linked together, for the 2nd list, there will be circle.

* file name cannot be `string.py`

##Reference

[1] [Pythonic](https://www.python.org/dev/peps/pep-0008/#indentation)
