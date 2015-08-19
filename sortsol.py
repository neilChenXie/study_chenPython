import pdb

class Solution:
    def largestNumber(self, nums):
        '''find the largest combination'''
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x,y:cmp(y+x,x+y))
        return ''.join(nums).lstrip('0') or '0'
