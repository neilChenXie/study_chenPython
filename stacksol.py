import pdb

class Solution:
	def trap(self, height):
		'''leftMax, rightMax, smaller is used to cumulate, larger is used to make sure'''
		leftMax = 0
		rightMax = 0
		i = 0
		j = len(height) - 1
		res = 0
		while i <= j:
			if leftMax >= rightMax:
				rightMax = rightMax if height[j] <= rightMax else height[j]
				res += rightMax - height[j]
				j -= 1
			else:
				leftMax = leftMax if height[i] <= leftMax else height[i]
				res += leftMax - height[i]
				i += 1
		return res
