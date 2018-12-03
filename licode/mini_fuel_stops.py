class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        step=0
        from Queue import PriorityQueue
        q=PriorityQueue()
        ind=0
        curr=startFuel
        while True:
            if curr>=target: return step
            while ind<len(stations) and stations[ind][0]<=curr: # add stations to q for later use
                q.put(-stations[ind][1])
                ind+=1
            if q.empty(): return -1
            curr+=-q.get() # add the most fuel as we do not reach yet
            step+=1

print Solution().minRefuelStops(100,
10,
[[10,60],[20,30],[30,30],[60,40]])
