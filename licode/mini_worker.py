import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        #
        workers = sorted([float(wage[i])/quality[i], quality[i]] for i in range(len(quality)))
        res,qsum = float('inf'),0
        heap = []

        for i in range(len(workers)):
        	#
            r,q = workers[i]
            heapq.heappush(heap,-q)
            #
            qsum += q
            if len(heap) > K:
            	# discard highest quality
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

print Solution().mincostToHireWorkers([10,20,5],[70,50,30], 2)
