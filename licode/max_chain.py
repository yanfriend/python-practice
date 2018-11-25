class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x:x[1])
        n=len(pairs)
        ret=0
        i=0
        while i<n:
            currend=pairs[i][1]
            ret+=1
            while i+1<n and pairs[i+1][0]<=currend: i+=1
            i+=1
        return ret

print Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])
