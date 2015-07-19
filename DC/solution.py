import pdb

class Solution:
    def majorityElement(self, nums):
        #hashtable
        i = 0
        counter = {}
        leng = len(nums)
        while i < leng:
            mapKey = nums[i]
            if mapKey not in counter:
                counter[mapKey] = 1
                i += 1
                continue
            else:
                counter[mapKey] += 1
                if counter(mapKey) > leng / 2:
                    return mapKey
