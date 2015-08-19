import pdb
import heapq

class Solution:
    def combine(self, n, k):
        self.res = []
    def __doIt(self, tmp, i, k, n):
        if k == 0:
            self.res.append(list(tmp))
            return
        else:
            while i < n:
                tmp.append(i)
                self.__doIt(tmp, i + 1, k - 1, n)
                tmp.pop()
                i += 1
            return
#    def combinationSum3(self, k, n):
#        ''' k 1~9 get n'''
#        self.res = []
#        tmpRes = []
#        self.__doComb3(tmpRes, k, n, i)
#    def __doComb3(self, tmpRes, k, n, i):
#        if n == 0 and k == 0:
#            self.res.append[list(tmpRes)]
#            return
#        elif k == 0 or n == 0:
#            return
#        else:
#            while i < 9:
#                nN = n - i
#                i += 1
#                if nN < 0:
#                    return
#                else:
#                    tmpRes.append(i)
#                    self.__doComb3(tmpRes, k - 1, nN, i)
#                    tmpRes.pop()
#            return
#    def combinationSum2(self, candidates, target):
#        '''the Answer is in leetcode'''
#        self.res = []
#        self.__doComb(target, candidates, [], 0)
#        return self.res
#    def __doComb(self, target, candidates, tmpRes, i):
#        if target == 0:
#            self.res.append(list(tmpRes))
#        elif target > 0:
#            while i < len(candidates):
#                tmpRes.append(candidates[i])
#                self.__doComb(target - candidates[i], candidates,tmpRes , i + 1)
#                i += 1
#        return
#    def combinationSum(self, candidates, target):
#        '''try all possible combination'''
#        self.res = []
#        tmpRes = []
#        self.__doTry(target, candidates, tmpRes, 0)
#        return self.res
#    def __doTry(self, target, candidates, tmpRes, i):
#        if target == 0:
#            self.res.append(list(tmpRes))
#            return
#        elif target < 0:
#            return
#        else:
#            while i < len(candidates):
#                #DFS start with itself
#                tmpRes.append(candidates[i])
#                self.__doTry(target - candidates[i], candidates, tmpRes, i)
#                tmpRes.pop()
#                i += 1
#            return
#    def findPeakElement(self, nums):
#        '''find the peak element, nums[-1] == nums[n] == -infinite'''
#        if not nums:
#            return []
#        tl = len(nums) - 1
#        i = 0
#        upFlag = True
#        res =[]
#        while i < tl:
#            if nums[i] > nums[i + 1] and upFlag:
#                res.append(i)
#                upFlag = False
#            elif nums[i] < nums[i + 1]:
#                upFlag = True
#            else:
#                #equal
#                upFlag = False
#            i += 1
#        if upFlag:
#            res.append(tl)
#        return res[0]
#    def majorityElement(self, nums):
#        '''find out elements more than 1/3
#        there are one or two elements can be returned
#        once they are majority, they can eliminate minority'''
#        if not nums:
#            return []
#        candi1, candi2, count1, count2 = None, None, 0, 0
#        for i in nums:
#            if i == candi1:
#                count1 += 1
#            elif i == candi2:
#                count2 += 1
#            elif count1 == 0:
#                candi1 = i
#                count1 += 1
#            elif count2 == 0:
#                candi2 = i
#                count2 += 1
#            else:
#                count1 -= 1
#                count2 -= 1
#        res = []
#        for n in [candi1, candi2]:
#            if nums.count(n) > len(nums) / 3:
#                res.append(n)
#        return res
#
#
#    def maxProfit(self, prices):
#        '''TODO: not finished'''
#        #find all min and max, strip origin array
#        minAry = []
#        maxAry = []
#        h = 1
#        tl = len(prices)
#        mf = True
#        while h < tl:
#            if mf and prices[h] > prices[h - 1]:
#                #find min
#                minAry.append(prices[h - 1])
#                mf = False
#            elif not mf and prices[h] < prices[h - 1]:
#                #find max
#                maxAry.append(prices[h - 1])
#                mf = True
#            #skip others
#            h += 1
#        if not mf:
#            maxAry.append(prices[-1])
#        i = 1
#        tl = len(minAry)
#        if tl == 0:
#            return 0
#        pdb.set_trace()
#        min1 = minAry[0]
#        max1 = maxAry[0]
#        res = max1 - min1
#        min2 = 0
#        max2 = 0
#        while i < tl:
#            if min2 == max2 == 0:
#                #add one or integrate
#                if maxAry[i] - min1 > res + maxAry[i] - minAry[i]:
#                    max1 = maxAry[i]
#                else:
#                    min2 = minAry[i]
#                    max2 = maxAry[i]
#                res = max1 + max2 - min1 - min2
#            else:
#                if maxAry[i] > max2 and minAry[i] < min2:
#                    #2 must update to new
#                    if max2 > max1:
#                        max1 = max2
#                        min1 = min(min1, min2)
#                    else:
#                        if max2 - min2 >= max1 - min1:
#                            max1 = max2
#                            min1 = min2
#                elif maxAry[i] < max2 and minAry[i] > min2:
#                    #because 1 want to
#                    if maxAry[i] - minAry[i] > max1 - min1:
#                        max1 = max2
#                        min1 = min2
#                        max2 = maxAry[i]
#                        min2 = minAry[i]
#                elif maxAry[i] > max2:
#                    #2 want to combine
#                    if maxAry[i] - min2 > maxAry[i] - minAry[i]:
#
            #CANNOT update Separately
            ##update 2: 
            #tmpMin2 = -1
            #tmpMax2 = -1
            ##min2 == max2 == 0: add
            #if min2 == max2 == 0 :
            #    tmpMax2 = max2
            #    tmpMin2 = min2
            #    max2 = maxAry[i]
            #    min2 = minAry[i]
            #elif maxAry[i] > max2 and minAry[i] > min2:
            #    max2 = maxAry[i]
            #elif maxAry[i] > max2 and minAry[i] < min2:
            #    tmpMax2 = max2
            #    tmpMin2 = min2
            #    max2 = maxAry[i]
            #    min2 = minAry[i]
            #else:
            #    #maxAry[i] <= max2
            #    if maxAry[i] - minAry[i] >= max2 - min2:
            #        tmpMax2 = max2
            #        tmpMin2 = min2
            #        max2 = maxAry[i]
            #        min2 = minAry[i]
            #    elif maxAry[i] - minAry[i] > max1 - min1:
            #        #not because 2 want to move, it's 1 too small
            #        tmpMax2 = max2
            #        tmpMin2 = min2
            #        max2 = maxAry[i]
            #        min2 = minAry[i]
            #res = max2 + max1 - min1 - min2
            ##update 1:
            #if tmpMin2 != -1:
            #    #update 1 when min2 updated, that is min2 == newMin
            #    if max2 - min1 > res:
            #        #integrated all together
            #        max1 = max2
            #        max2 = min2 = 0
            #    elif tmpMax2 > max1 and tmpMin2 > min1:
            #        max1 = tmpMax2
            #    elif tmpMax2 > max1 and tmpMin2 < min1:
            #        max1 = tmpMax2
            #        min1 = tmpMin2
            #    else:
            #        #tmpMax2 <= max1
            #        if tmpMax2 - tmpMin2 >= max1 - min1:
            #            max1 = tmpMax2
            #            min1 = tmpMin2
            #        #else no need to update
            #res = max2 + max1 - min1 - min2
#            i += 1
#        return res

#    def findMin(self, nums):
#        h = 0
#        t = len(nums) - 1
#        pdb.set_trace()
#        while h < t:
#            i = (h + t) / 2
#            if nums[i] > nums[t]:
#                h = i + 1
#            elif nums[i] < nums[t]:
#                t = i
#            else:
#                t -= 1
#        return nums[h]
#    def canJump(self, nums):
#        i = len(nums) - 2
#        tmp = 1
#        res = False
#        while i > 0:
#            if nums[i] < tmp:
#                tmp += 1
#                res = False
#            else:
#                tmp = 1
#                res = True
#            i -= 1
#        return res
#    def minSubArrayLen(self, s, nums):
#        init = 0
#        res = 0
#        h = 0
#        t = 0
#        res = 0
#        for (i, var) in enumerate(nums):
#            if var >= s:
#                return 1
#            else:
#                init += var
#                t = i
#                if init >= s:
#                    #find the new h position
#                    while init - nums[h] >= s:
#                        init -= nums[h]
#                        h += 1
#                    tmpLen = t - h + 1
#                    res = res if res < tmpLen and res != 0 else tmpLen
#        return res
#
#    def minPathSum(self, grid):
#        '''from top left to buttom right'''
#        for (x, row) in enumerate(grid):
#            for (y, var) in enumerate(row):
#                if x == 0 and y > 0:
#                    grid[x][y] += grid[x][y - 1]
#                elif y == 0 and x > 0:
#                    grid[x][y] += grid[x - 1][y]
#                elif y != 0 and x != 0:
#                    grid[x][y] += min(grid[x-1][y], grid[x][y-1])
#                else:
#                    continue
#        try:
#            return grid[-1][-1]
#        except IndexError:
#            return None
#
#    def removeDuplicates(self, nums):
#        '''remain at most 2'''
#        tl = len(nums)
#        if tl <= 2:
#            return tl
#        h1 = 0
#        h2 = 1
#        dupFlag = True
#        while h2 < tl:
#            if dupFlag:
#                h1 += 1
#                nums[h1] = nums[h2]
#                if nums[h1] == nums[h1 - 1]:
#                    dupFlag = False
#            else:
#                if nums[h2] != nums[h1]:
#                    h1 += 1
#                    nums[h1] = nums[h2]
#                    dupFlag = True
#            h2 += 1
#        return h1 + 1
#    def searchMatrix(self, matrix, target):
#        ''' search in sorted 2D matrix'''
#        #search first col
#        h = 0
#        t = len(matrix) - 1
#        while h <= t:
#            i = (h + t) / 2
#            if matrix[i][0] == target:
#                return True
#            elif matrix[i][0] > target:
#                t = i - 1
#            elif:
#                h = i + 1
#        if t > 0:
#            hh = 0
#            tt = len(matrix[t]) - 1
#            while hh <= tt:
#                ii = (hh + tt) / 2
#                if matrix[t][ii] == target:
#                    return True
#                elif matrix[t][ii] > target:
#                    tt = ii - 1
#                else:
#                    hh = ii + 1
#        return False
#
#        def search2(self, nums, target):
#            '''with duplicate'''
#            h = 0
#            t = len(nums) - 1
#            while h < t:
#                i = (h + t) / 2
#                if nums[i] == target:
#                    return True
#                elif nums[i] > nums[h]:
#                    #left side is sorted
#                    if target >= nums[h] and target < nums[i]:
#                        t = i - 1
#                    else:
#                        h = i + 1
#                elif nums[i] < nums[t]:
#                    #right side is sorted
#                    if target <= nums[t] and target > nums[i]:
#                        h = i + 1
#                    else:
#                        t = i - 1
#                elif nums[i] > nums[t] and nums[i] < nums[h]:
#                    return False
#                elif :
#                    h += 1
#	def search(self, nums, target):
#	    '''search in rotated sorted ary'''
#	    minI = self.__bsMin(0, len(nums) - 1, nums)
#	    if target <= nums[-1]:
#	        return self.__doBS(minI, len(nums) - 1, nums, target)
#	    else:
#	        return self.__doBS(0, minI - 1, nums, target)
#	def __bsMin(self, h, t, nums):
#	    if nums[h] < nums[t]:
#	    	return h
#	    while h < t:
#	    	i = (h + t) / 2
#	    	if nums[i] < nums[t]:
#	    		t = i
#	    	elif nums[i] >= nums[h]:
#	    		h = i + 1
#	    return h
#	def __doBS(self, h, t, nums, target):
#	    while h <= t and target <= nums[t] and target >= nums[h]:
#	        i = (h + t) / 2
#	        if nums[i] > target:
#	            t = i - 1
#	        elif nums[i] < target:
#	            h = i + 1
#	        else:
#	            return i
#	    return -1
#	def subsets(self, nums):
#		res = [[]]
#		for var in nums:
#			tmp = list(res)
#			for ele in tmp:
#				nele = list(ele)
#				nele.append(var)
#				res.append(nele)
#		return res
#	def subsetsWithDup(self, nums):
#		res = [[]]
#		nums.sort()
#		pre = None
#		tmp = []
#		for var in nums:
#			i = 0
#			if var == pre:
#				tl = len(tmp)
#				nTmp = []
#				while i < tl:
#					nEle = list(tmp[i])
#					nEle.append(var)
#					res.append(nEle)
#					nTmp.append(nEle)
#					i += 1
#				tmp = nTmp
#			else:
#				pre = var
#				tl = len(res)
#				tmp = []
#				while i < tl:
#					nEle = list(res[i])
#					nEle.append(var)
#					res.append(nEle)
#					tmp.append(nEle)
#					i += 1
#		return res
#	def spiralOrder(self, matrix):
#		self.res = []
#		self.mat = matrix
#		if len(matrix) == 0:
#			return []
#		self.tb = 0
#		self.lb = 0
#		self.bb = len(matrix) - 1
#		self.rb = len(matrix[0]) - 1
#		self.__goRight(0, 0)
#		return self.res
#	def __goRight(self, x, y):
#		if self.tb > self.bb or self.lb > self.rb:
#			return
#		self.res.append(self.mat[x][y])
#		if y < self.rb:
#			self.__goRight(x, y + 1)
#		else:
#			self.tb += 1
#			self.__goDown(x + 1, y)
#	def __goLeft(self, x, y):
#		if self.tb > self.bb or self.lb > self.rb:
#			return
#		self.res.append(self.mat[x][y])
#		if y > self.lb:
#			self.__goLeft(x, y - 1)
#		else:
#			self.bb -= 1
#			self.__goUP(x - 1, y)
#	def __goDown(self, x ,y):
#		if self.tb > self.bb or self.lb > self.rb:
#			return
#		self.res.append(self.mat[x][y])
#		if x < self.bb:
#			self.__goDown(x + 1, y)
#		else:
#			self.rb -= 1
#			self.__goLeft(x, y - 1)
#	def __goUP(self, x, y):
#		if self.tb > self.bb or self.lb > self.rb:
#			return
#		self.res.append(self.mat[x][y])
#		if x > self.tb:
#			self.__goUP(x - 1, y)
#		else:
#			self.lb += 1
#			self.__goRight(x, y + 1)
#	def generateMatrix(self, n):
#		ne = pow(n, 2)
#		i = 1
#		lb = 0
#		tb = 0
#		rb = n - 1
#		bb = n - 1
#		res = [[0 for x in range(n)] for x in range(n)]
#		x = 0
#		y = 0
#		df = 0
#		while i <= ne:
#			res[x][y] = i
#			if df == 0:
#				#right
#				if y < rb:
#					y += 1
#				else:
#					tb += 1
#					df = 1
#					x += 1
#			elif df == 1:
#				#down
#				if x < bb:
#					x += 1
#				else:
#					rb -= 1
#					df = 2
#					y -= 1
#			elif df == 2:
#				#left
#				if y > lb:
#					y -= 1
#				else:
#					bb -= 1
#					df = 3
#					x -= 1
#			else:
#				#up
#				if x > tb:
#					x -= 1
#				else:
#					lb += 1
#					df = 0
#					y += 1
#			i +=1
#		return res
#
#    def sortColors(self, nums):
#        if len(nums) == 0:
#            return
#        cur = p0 = p1 = p2 = 0
#        while cur < len(nums):
#            if nums[cur] == 2:
#                nums[p2] = 2
#                p2 +=1
#            elif nums[cur] == 1:
#                nums[p2] = 2
#                nums[p1] = 1
#                p2 += 1
#                p1 += 1
#            else:
#                nums[p0] = 0
#                nums[p2] = 2
#                nums[p1] = 1
#                p2 += 1
#                p1 += 1
#                p0 += 1
#            cur += 1
#        return
#    def twoSum(self, nums, target):
#        i = 0
#        numhash = {}
#        numLen = len(nums)
#        while i < numLen:
#            if not str(target - nums[i]) in numhash:
#                numhash[str(nums[i])] = i
#            else:
#                return [numhash[str(target - nums[i])], i]
#            i += 1
#    def fourSum(self, nums, target):
#        self.res = []
#        nums.sort()
#        self.nums = nums
#        pre = None
#        for (i, var) in enumerate(nums):
#            if var != pre:
#                self.__do3sum(i + 1, -var, [var])
#                pre = var
#        return self.res
#
#    def __do3sum(self, s, target, tmp):
#        pre = None
#        while s < len(self.nums):
#            if self.nums[s] != pre:
#                tmp.append(self.nums[s])
#                self.__do2sum(s + 1, target - self.nums[s], tmp)
#                tmp.pop()
#                pre = self.nums[s]
#            s += 1
#        return
#
#
#    def __do2sum(self, h, target, tmp):
#        t = len(self.nums) - 1
#        while h < t:
#            if self.nums[h] + self.nums[t] > target:
#                t -= 1
#            elif self.nums[h] + self.nums[t] < target:
#                h += 1
#            else:
#                tmp.append(self.nums[h])
#                tmp.append(self.nums[t])
#                if not tmp in self.res:
#                    self.res.append(list(tmp))
#                tmp.pop()
#                tmp.pop()
#                h += 1
#                t -= 1
#        return
#    def searchRange(self, nums, target):
#        t = len(nums) - 1
#        h = 0
#        tmpI = (h + t) / 2
#        while h <=t and h != tmpI:
#            tmpI = (h + t) / 2
#            if nums[tmpI] > target:
#                t = tmpI
#            elif nums[tmpI] < target:
#                h = tmpI
#            else:
#                tmpH = h
#                tmpT = t
#                while tmpH > 0 and nums[tmpH] == target:
#                    tmpH -= 1
#                while tmpT < len(nums) and nums[tmpH] == target:
#                    tmpT += 1
#                return [tmpH, tmpT]

#        return [-1, -1]
