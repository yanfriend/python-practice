class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        org_r=len(nums)
        org_c=len(nums[0])
        if org_r*org_c!=r*c: return nums

        rp=0; cp=0
        ret=[[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                import ipdb; ipdb.set_trace()
                if cp==c: cp=0;rp+=1
                ret[i][j]=nums[rp][cp]
                cp+=1
        return ret

print Solution().matrixReshape([[1,2],[3,4]],1,4)

