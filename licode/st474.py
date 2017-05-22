
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # double 0-1 backpack problem

        def count01(str):
            return str.count('0'), str.count('1')

        dp1=[[0]*(n+1)]*(m+1)  # vip, this is important

        dp2=[[0]*(n+1) for _ in range(m+1)]

        import ipdb; ipdb.set_trace()

        for str in strs:
            z,o=count01(str)

            import ipdb; ipdb.set_trace()

            for zeros in range(m,-1,-1):
                for ones in range(n,-1,-1):
                    if zeros>=z and ones>=o:
                        dp[zeros][ones]=max(dp[zeros][ones], dp[zeros-z][ones-o]+1)

        return dp[m][n]

print Solution().findMaxForm(["10","0001","111001","1","0"],5,3)
