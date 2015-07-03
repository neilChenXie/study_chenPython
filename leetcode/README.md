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

# Binary Tree and BST
