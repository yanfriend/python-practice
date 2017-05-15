class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num==0: return [0]
        if num==1: return [0,1]

        ret=[0]*(num+1)
        ret[0]=0
        ret[1]=1

        i=2
        while i<=num:
            prev_end=i
            for j in range(i,min(2*i,num)+1):
                ret[j]=ret[j-i]+1
            i=min(2*i,num)+1
        return ret

print Solution().countBits(4)
