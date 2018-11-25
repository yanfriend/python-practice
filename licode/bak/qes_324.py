import copy


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sorted=copy.deepcopy(nums)
        sorted.sort()

        n=len(sorted)
        fh=0; sh=n/2+1
        for i in range(n)[::-1]:
            if i%2==0: nums[i]=sorted[fh]; fh+=1
            else:
                nums[i]=sorted[sh]; sh+=1

        return

print Solution().wiggleSort([1,5,1,1,6,4])
