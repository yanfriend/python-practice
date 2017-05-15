class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l=max(nums)
        r=sum(nums)

        def can_split(mid):
            c=1
            s=0
            for num in nums:
                s += num
                if s>mid:
                    s=num
                    c+=1
            return c<=m

        while (l<r):
            mid=l+(r-l)/2

            import ipdb; ipdb.set_trace()

            if can_split(mid):
                r=mid
            else:
                l=mid+1
        return l




print Solution().splitArray([1,2147483647],2)
