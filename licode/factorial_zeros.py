class Solution:
    def preimageSizeFZF(self, K):
        return self.binarySearch(K)-self.binarySearch(K-1)

    def binarySearch(self, k):
        if k<0: return 0
        l=0; r=5*k+5
        while (l<r):
            mid=(l+r)/2
            val = self.trailingzero(mid)
            if val>k:
                r=mid
            else: l=mid+1
        return l

    def trailingzero(self, n): # how many 0's in n factorial
        ans=0
        while n>0:
            ans+=n/5
            n/=5
        return ans

    """
    def preimageSizeFZF(self, K):
        def nzero(n):
            f = 5
            cnt = 0
            while f <= n:
                cnt += n // f
                f *= 5
            return cnt

        if K == 0:
            return 5

        min = 1
        max = K * 5
        while min < max:
            mid = (min + max) // 2
            if nzero(mid) < K:
                min = mid + 1
            else:
                max = mid

        if nzero(min) != K:
            return 0
        else:
            # next = (min // 5 + 1) * 5
            # return next - min
            return 5
    """

# print Solution().preimageSizeFZF(1) # ans: 5, number 5,6,7,8,9
print Solution().preimageSizeFZF(0) # ans: 5, number 5,6,7,8,9

