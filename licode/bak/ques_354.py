class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0

        def cmp_fn(a,b):
            if a[0]!=b[0]:
                return a[0]-b[0]
            else:
                return b[1]-a[1]

        envelopes.sort(cmp=cmp_fn) # properly sorted envelopes

        # find the longest increasing subsequence by a[1]

        tails=[envelopes[0][1]]
        for i in range(1,len(envelopes)):
            # fin env[i]'s insert position
            l=0; r=len(tails)
            while l<r:
                mid=(l+r)/2
                if envelopes[i][1]>tails[mid]:
                    l=mid+1
                else:
                    r=mid

            if l>=len(tails):
                tails.append(envelopes[i][1])
            else:
                tails[l]=envelopes[i][1]
        return len(tails)


        # below is correct, but timeout
        '''
        ret=1
        dp=[1]*len(envelopes)
        for i in range(1,len(envelopes)):
            for j in range(0,i):
                if envelopes[j][1]<envelopes[i][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        '''


print Solution().maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])
