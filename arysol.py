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
    def twoSum(self, nums, target):
        i = 0
        numhash = {}
        numLen = len(nums)
        while i < numLen:
            if not str(target - nums[i]) in numhash:
                numhash[str(nums[i])] = i
            else:
                return [numhash[str(target - nums[i])], i]
            i += 1
    def fourSum(self, nums, target):
        self.res = []
        nums.sort()
        self.nums = nums
        pre = None
        for (i, var) in enumerate(nums):
            if var != pre:
                self.__do3sum(i + 1, -var, [var])
                pre = var
        return self.res

    def __do3sum(self, s, target, tmp):
        pre = None
        while s < len(self.nums):
            if self.nums[s] != pre:
                tmp.append(self.nums[s])
                self.__do2sum(s + 1, target - self.nums[s], tmp)
                tmp.pop()
                pre = self.nums[s]
            s += 1
        return


    def __do2sum(self, h, target, tmp):
        t = len(self.nums) - 1
        while h < t:
            if self.nums[h] + self.nums[t] > target:
                t -= 1
            elif self.nums[h] + self.nums[t] < target:
                h += 1
            else:
                tmp.append(self.nums[h])
                tmp.append(self.nums[t])
                if not tmp in self.res:
                    self.res.append(list(tmp))
                tmp.pop()
                tmp.pop()
                h += 1
                t -= 1
        return
    def searchRange(self, nums, target):
        t = len(nums) - 1
        h = 0
        tmpI = (h + t) / 2
        while h <=t and h != tmpI:
            tmpI = (h + t) / 2
            if nums[tmpI] > target:
                t = tmpI
            elif nums[tmpI] < target:
                h = tmpI
            else:
                tmpH = h
                tmpT = t
                while tmpH > 0 and nums[tmpH] == target:
                    tmpH -= 1
                while tmpT < len(nums) and nums[tmpH] == target:
                    tmpT += 1
                return [tmpH, tmpT]
        return [-1, -1]
