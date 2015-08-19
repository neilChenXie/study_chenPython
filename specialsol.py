import pdb
import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        '''topological search /w DFS or BFS'''
        #create directed graph
        needs = [0 for x in range(numCourses)]
        flow = [set([]) for i in range(numCourses)]
        for var in prerequisites:
            flow[var[1]].add(var[0])
            needs[var[0]] += 1
        #pdb.set_trace()
        zeros = collections.deque()
        for (i,var) in enumerate(needs):
            if var == 0:
                zeros.append(i)
        i = 0
        while i != len(zeros):
            node = zeros[i]
            i += 1
            for var in flow[node]:
                needs[var] -= 1
                if needs[var] == 0:
                    zeros.append(var)
            if len(zeros) == numCourses:
                return True
        return False
