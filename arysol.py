import ipdb
import sys
import heapq
import collections
import string
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target > nums[-1] and target < nums[0]:
            return False
        elif target == nums[0] or target == nums[-1]:
            return True
        h = 0
        t = len(nums) - 1
        # ipdb.set_trace()
        while h <= t:
            m = h + ((t - h) >> 1)
            if nums[m] == target:
                return True
            elif nums[m] < nums[t]:
                if target > nums[m] and target <= nums[t]:
                    h = m + 1
                else:
                    t = m - 1
            elif nums[m] > nums[h]:
                if target < nums[m] and target >= nums[h]:
                    t = m - 1
                else:
                    h = m + 1
            elif nums[h] == target:
                return True
            else:
                h += 1
        return False
