
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)

        from Queue import PriorityQueue
        pq = PriorityQueue()

        for i in range(n):
            pq.put((A[i]*1.0/A[n-1], i, n-1))

        while K > 1:
            K -= 1
            _, r, c = pq.get()
            print 'get', [A[r],A[c]]

            print 'put',  [A[r],A[c-1]]
            pq.put((A[r]*1.0/A[c-1], r, c - 1))
        _, r, c = pq.get()
        return [A[r], A[c]]




"""
        n=len(A)

        class Fraction(object):
            def __init__(self, pair):
                self.pair = pair

            def __cmp__(self, other):
                return cmp(A[self.pair[0]] * A[n-1-other[1]],
                           A[other[0]] * A[n-1-self.pair[1]])

            def __getitem__(self, key): # needed otherwise indexing error
                return self.pair[key]


        from Queue import PriorityQueue
        pq=PriorityQueue()

        for i in range(n):
            pq.put(Fraction((i,0)))

        while K>1:
            K-=1
            r, c = pq.get()
            if c<n-1:
                pq.put((r,c+1))
        r, c = pq.get()
        return [A[r],A[n-1-c]]
"""


# print Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3)  # Output: [2, 5])
# print Solution().kthSmallestPrimeFraction([1,13,17,59], 6)  # 13,17
print Solution().kthSmallestPrimeFraction([1,3,11,13,37,53,59], 6)  # 1,13
