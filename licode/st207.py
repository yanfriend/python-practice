import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        cnt=0
        indegrees=[0]*numCourses
        for pre in prerequisites:
            indegrees[pre[0]]+=1

        qu=collections.deque() # dont use Queue, use this one please
        for i,d in enumerate(indegrees): # add to q course_id, not indegree number
            if not d:
                qu.append(i)
                cnt+=1

        while qu:
            cs=qu.popleft()
            for pre in prerequisites:
                if pre[1]==cs:
                    indegrees[pre[0]]-=1

                    if indegrees[pre[0]]==0:
                        qu.append(pre[0])
                        cnt+=1
        return cnt==numCourses

print Solution().canFinish(2,[[0,1]])
