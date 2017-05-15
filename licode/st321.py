class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums1)+len(nums2)<k:
            return []

        ret=[float('-inf')]*k
        for i in range(0,len(nums1)+1):
            if k-i>len(nums2): continue

            ns1=self.selectk(nums1,i)
            ns2=self.selectk(nums2,k-i)
            tmp=self.mergek(ns1,ns2,k)
            if len(tmp)<k: continue
            ret=self.maxk(ret,tmp)
        return ret

    def maxk(self,ns1,ns2):
        for i in range(len(ns1)):
            if ns1[i]>ns2[i]:
                return ns1
            elif ns1[i]<ns2[i]:
                return ns2
        return ns1

    def mergek(self,ns1,ns2,k):
        ret=[]
        i=j=0
        while i<len(ns1) and j<len(ns2):
            if self.comparek(ns1,i,ns2,j):
                ret.append(ns1[i])
                i+=1
            else:
                ret.append(ns2[j])
                j+=1
        ret += ns1[i:]+ns2[j:]
        return ret

    def comparek(self,ns1,i,ns2,j):
        while i<len(ns1) and j<len(ns2) and ns1[i]==ns2[j]:
            i+=1; j+=1
        if j==len(ns2): return True               # j is at end, ns1 is larger;
        return i<len(ns1) and ns1[i]>ns2[j]

    def selectk(self,nums,k):
        if len(nums)<k or k==0:
            return []
        ret=[float('inf')]
        for i,num in enumerate(nums):
            while num>ret[-1] and len(nums)-i>k-len(ret)+1:
                ret.pop()
            if len(ret)<k+1: ret.append(num)
        return ret[1:]

print Solution().maxNumber([6,7,5], [4,8,1], 3)
