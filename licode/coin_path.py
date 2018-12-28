class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        n=len(A)
        cost=[float('inf')]*(n+1); cost[1] = A[0]
        prev=[-1]*(n+1)

        for i in range(2,n+1):
            if A[i-1]==-1: continue # not reachable

            for j in range(B,-1,-1):
                k=i-j
                if k<1: continue  # k is descreasing
                if A[k-1]==-1: continue

                if cost[i]>cost[k]+A[i-1]: # as k is increasing, if equlas, log the smaller one only
                    # small bug on path
                    cost[i]=cost[k]+A[i-1]
                    prev[i]=k

        if cost[n]==float('inf'): return []

        ret=[]
        p=n
        while p>0:
            ret.append(p)
            p=prev[p]
        return ret[::-1]

print Solution().cheapestJump([1,2,4,-1,2], 2) # [1,3,5]
print Solution().cheapestJump([1,2,4,-1,2], 1) # []

