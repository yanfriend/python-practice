import bisect

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        return self.helper(stones,0,0)

    def helper(self,stones,ind,k):
        if ind==len(stones)-1: return True
        for j in (k-1,k,k+1):
            if j<=0: continue
            next_ind=bisect.bisect_left(stones,stones[ind]+j,ind+1,len(stones))

            print 'current ind:{}, next_val:{}, next_ind:{}'.format(ind, stones[ind]+j,next_ind)
            # import ipdb;ipdb.set_trace()

            if next_ind>=len(stones) or stones[next_ind]!=stones[ind]+j: continue
            if self.helper(stones,next_ind,j): return True
        return False

# print Solution().canCross([0,1,3,5,6,8,12])
print Solution().canCross([0,1,3,5,6,8,12,17])
