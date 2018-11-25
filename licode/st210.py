import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ret=[]
        indegrees=[0]*numCourses
        qu=collections.deque()

        for pre in prerequisites:
            indegrees[pre[0]]+=1
        qu.extend([i for i,v in enumerate(indegrees) if v==0])

        while qu:
            cs=qu.popleft()
            ret.append(cs)

            for pre in prerequisites:
                if pre[1]==cs:
                    indegrees[pre[0]]-=1
                    if indegrees[pre[0]]==0:
                        qu.append(pre[0])
        return ret if len(ret)==numCourses else []

print Solution().findOrder(2,[[1,0]])
