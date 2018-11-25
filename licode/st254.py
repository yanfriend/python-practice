class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        ret=[]
        self.helper(2,1,n,ret,[])
        return ret

    def helper(self,start,prod,n,ret,path):
        if prod==n: ret.append(path); return
        if prod>n or start>n: return

        for i in range(start,n):
            if i*prod>n: break
            if n%i==0:
                self.helper(i,prod*i,n,ret,path+[i])
        return

print Solution().getFactors(12)
#print Solution().getFactors(37)
#print Solution().getFactors(32)
