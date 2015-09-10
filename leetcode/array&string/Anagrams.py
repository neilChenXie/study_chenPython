import collections
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    thinking: each group should have their unique char combination, e.g:{("e","a","t"):['eat','ate']}, the problem become how to eastablish the hash table. However, the key is order-sensitive.
    Solution: each time sort the tuple.
    debug: time exceed? sorted(word) = list
           lexicographic order? sorted()
    
    """
    res = []
    comb = collections.defaultdict(list)
    for word in strs:
        # tmp = []
        # for char in word:
            # tmp.append(char)
        # tmp.sort()
        # comb[tuple(tmp)].append(word)
        comb["".join(sorted(word))].append(word)
    for key in comb:
        res.append(sorted(comb[key]))
    return res
