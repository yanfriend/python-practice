import collections


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def countLess(A, K):
            res = 0
            d = collections.Counter()
            i = 0

            for j in range(len(A)):
                d[A[j]] += 1
                if d[A[j]] == 1: K -= 1  # A[j] is a new number.
                while K < 0:  # no capacity for K
                    d[A[i]] -= 1
                    if d[A[i]] == 0: K += 1  # claim one for K capacity
                    i += 1
                res += j - i + 1
            return res

        return countLess(A, K) - countLess(A, K - 1)


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
