class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        import collections
        fd = collections.defaultdict(dict)
        for f in flights:
            fd[f[0]][f[1]] = f[2]

        from Queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((0, src, K+1))

        while (pq.qsize() > 0):
            p, node, step = pq.get()
            if node == dst: return p
            if step == 0: continue
            for j in fd[node]:
                pq.put((p + fd[node][j], j, step - 1))
        return -1

print Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
