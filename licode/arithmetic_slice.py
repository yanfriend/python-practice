import collections

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp=[collections.defaultdict(int) for _ in range(len(A))]
        ret=0

        for i in range(len(A)):
            for j in range(i):
                diff=A[i]-A[j]
                ret+=dp[j][diff]
                dp[i][diff]+=dp[j][diff]+1
            # print dp
        return ret

print Solution().numberOfArithmeticSlices([2,4,6,8])
print Solution().numberOfArithmeticSlices([2,4,6,8,10])
