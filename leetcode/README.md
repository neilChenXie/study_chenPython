#Data Structure & Algorithm

##General
* Full Adder

| 1st \ 2nd | has c | no c |
| --- | ----- | ---- |
| **same length** | create one more node with 1 | finished |
| **different length** | extra + 1, then append | append extra to tail directly |

##Link list

* Basic:
    * single/double
    * add/delete
* Characteristic
    * Head pointer is different with others
    * Single:
        * Cannot go back!
* Tricks:
    * Use `dummyHead` when needed
    * Reverse single link list

        > 3 pointers

    * **n** to last
        > 2 pointers<br>
        > edge case: none/one element only<br>
        > rm: the 1st is different

    * find the middle of single link list

        > 2 pointers, 1st 2 steps/circle, then 2nd 1 step. Finally, 2nd move 1 more step to the start of second half.

    * check/detect link list cycle

        > 1. fast pointer 2 steps while slow pointer 1 step, if catch up, True, else False

        > 2. after checking, new pointer start from head, old start from meet point, one step each, they will meet at the beginning of loop

## Tree, Binary Tree and BST

###Concept

* **hierarchy**, **logical model**, **recursive** data structure

* phrase

    > root, children, parent, sibling, leaf, ancestor, descendent<br>
    Depth/Height of nodes

* application

    > File system<br>
    Organize data<br>
    Dictionary structure

###Binary Tree

####Concept

* cannot have more than 2 children
    > link list is also BT

* **strict** (or **proper**) BT with nodes only have 0 or 2 children

* **complete** BT with all levels except prossibly the last one completely filled and all nodes are as left as possible

* **perfect** BT = full complete BT

* **Balanced** BT: minimal height overall. heightRight - heightLeft <= 1
    > no child == -1<br>
    > 1 child == 0

####Characteristic

* max no. of nodes at level i (root i = 0):
    > 2^i

* max no. of nodes of **perfect** BT:
    > 2^0 + 2^1 + ... + 2^h = 2 ^ (h + 1) - 1 = 2 ^ height - 1

* calcu height with known node no.
    > max: n-1 (link list)<br>
    min: log2(n) (complete BT)

* **complete** BT with array implementation:
    > left child: 2 \* i + 1<br>
    right child: 2 \* i + 2<br>
    **app**: heaps

####Tricks

* DFS without recursive

###BFS

* Question

    * word labber

        > scan dictionary: n * dictLen * wordLen
        scan Alphabet： n * 26 * wordLen
        Therefore, it's depends on the dictLen

    * surrounded region

        > triggerQ & mapSet. check before delete, BFS.
        cannot modify string in Python

    * numIslands

        > '1' not 1
