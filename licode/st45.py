class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        max_reach=0
        i=0

        while max_reach<len(nums)-1:
            next_reach=max_reach
            while i<=max_reach:
                next_reach=max(next_reach,i+nums[i])
                i+=1

            ret+=1
            max_reach=next_reach
        return ret

print Solution().jump([1,2,3])  # expect 2
