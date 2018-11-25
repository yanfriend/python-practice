import Queue

class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        q=Queue.PriorityQueue()
        projects=sorted(zip(Capital,Profits))[::-1]  # sorted by Capital, descreasing.

        for _ in range(k):
            while projects and projects[-1][0]<=W:
                q.put(-projects.pop()[1])
            if not q.empty():
                W-=q.get()
        return W


# print ipo(k=2, W=0, Profits=[1,2,3], Capital=[0,1,1])

print ipo(k=1, W=0, Profits=[1,2,3], Capital=[1,1,2])
