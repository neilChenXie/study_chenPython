#Data Structure & Algorithm

##General

* Full Adder

| 1st \ 2nd | has c | no c |
| --- | ----- | ---- |
| **same length** | create one more node with 1 | finished |
| **different length** | extra + 1, then append | append extra to tail directly |

##Array

* Remove duplicate

	* 2 or 3 pointers, slow and fast

* Binary search

	* finally h == insert position, t == h - 1
		```py
		h = 0
		t = len(ary) - 1
		while h <= t:
			i = (h + t) / 2
			if ary[i] == target:
				return i
			elif ary[i] > target:
				t = i - 1
			else:
				h = i + 1
		#ary[h] is bigger than target and ary[t] is smaller than target
		#if h = len(ary): need resize origin ary
		#if t < 0: the 1st element is bigger than target
		```
	* rotated ary
		```py
		h = 0
		t = len(ary) - 1
		while h < t:
			i = (h + t) / 2
			if ary[i] == target:
				return i
			elif ary[i] > ary[h]:
				#left side is sorted, no mater there is duplicate or not
				if target > ary[h] and target < ary[i]:
					#do BS
				else:
					h = i + 1
			elif ary[i] < ary[t]:
				#right side is sorted, no mater there is duplicate or not
				if target < ary[t] and target > ary[i]:
					#do BS
				else:
					t = i - 1
			elif target > ary[t] and target < ary[h]:
				return -1
			else:
				#equal to ary[h] or ary[t]
				if ary[h] == target:
					return h
				else:
					h += 1
		```

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


## Binary Search

### Prerequist

* Sorted Array

### Template

```py
	'''
	normally, can handle duplicate
	Q: insertation, fistBadVersion
	'''
	ary.sort()
	h = 0
	t = len(ary) - 1 #use index not length
	while h <= t:
		'''
		1. not (h + t) >> 1 in case of sum overflow
		2. >> 1 instead of >>2
		3. >> if lower than +, need +(>>1)
		'''
		m = h + ((t - h) >> 1)
		if ary[m] == target:
			return m
		elif ary[m] < target:
			h = m + 1
		else:
			t = m - 1
	'''
	h may equal to len(ary) or 0
	or ary[h] is just bigger than target
	'''
	return h
	'''
	because h + ((t - h) >> 1) floor to h.
	trick: h + ((t - h + 1) >> 1) floor to t. index t is just less than target
	'''
```

### Trick

```py
	'''
	find target in rotated sorted without/with duplicate
	edge: target < nums[0] and > nums[-1], exist in vaccum
	rotated: 
		array become 2 part:
		1. nums[m] > nums[h] left part
		2. nums[m] < nums[t] right part
		3. nums[m] == nums[h] undecided
		in situation 1: target in h~m, then simplify to normal BS, otherwise, h = m + 1
		similarly, for situation 2: target in m~t, then simplify to normal BS, otherwise, t = m - 1
		for undecided, chech if nums[h] == target, otherwise h = h + 1

		first check target == nums[m] or target == nums[t] or target == nums[h]
	'''
```

## BFS

### Template

```py
	# double direction BFS

```

### Question

* word labber

    > scan dictionary: n * dictLen * wordLen
    scan Alphabet： n * 26 * wordLen
    Therefore, it's depends on the dictLen

* surrounded region

    > triggerQ & mapSet. check before delete, BFS.
    cannot modify string in Python

* numIslands

    > '1' not 1

## General Tricks

* find range of the same value
	```py
	h = t = index
	while h > 0 and ary[h - 1] == target:
		h -= 1
	while t < len(ary) - 1 and ary[t+1] == target:
		t += 1
	return [h,t]
	```
