import pdb

class Solution:
    def candy(self, ratings):
        '''with higher rate, get more candy than neighbors'''
        #use O(n) time and O(n) space
        #the peak is count duplicated
        #if not ratings:
        #    return 0
        #res = 0
        #pre = 1
        #preRate = ratings[0]
        #for i in ratings:
        #    if i > preRate:
        #        #only for highter
        #        pre += 1
        #        res += pre
        #        preRate = i
        #    else:
        #        preRate = i
        #        pre = 0
        ##now pre store last value
        #for i in reversed(ratings):
        #    if i > preRate:
        #        #only for higher
        #        pre += 1
        #        res += pre
        #        preRate = i
        #    else:
        #        pre = 0
        #        preRate = i
        #return res + len(ratings)

#	def canCompleteCircuit(self, gas, cost):
#		left = [0 for i in range(len(gas))]
#		tmp = 0
#		reci = 0
#	def canCompleteCircuit(self, gas, cost):
#		left = [0 for i in range(len(gas))]
#		tmp = 0
#		reci = 0
#		for (i,var) in enumerate(gas):
#			left[i] = var - cost[i]
#			tmp += left[i]
#			if tmp < 0:
#				reci = i + 1
#				tmp = 0
#		if reci >= len(gas):
#			return -1
#		i = 0
#		while i < reci:
#			tmp += left[i]
#			if tmp < 0:
#				return -1
#			i += 1
#		return reci
