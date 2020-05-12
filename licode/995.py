class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ret = 0
        hints = [0] * len(A)
        flip = 0

        for i in range(len(A)):

            import ipdb; ipdb.set_trace()

            flip ^= hints[i]
            if flip == A[i]:
                ret += 1
                flip ^= 1
                if i + K > len(A): return -1
                if i + K < len(A): hints[i + K] ^= 1
        return ret

print(Solution().minKBitFlips([0,1,0], 1))
