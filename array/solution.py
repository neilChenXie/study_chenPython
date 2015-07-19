import pdb

class Solution:
    def sortColors(self, nums):
        if len(nums) == 0:
            return
        cur = p0 = p1 = p2 = 0
        while cur < len(nums):
            if nums[cur] == 2:
                nums[p2] = 2
                p2 +=1
            elif nums[cur] == 1:
                nums[p2] = 2
                nums[p1] = 1
                p2 += 1
                p1 += 1
            else:
                nums[p0] = 0
                nums[p2] = 2
                nums[p1] = 1
                p2 += 1
                p1 += 1
                p0 += 1
            cur += 1
        return

