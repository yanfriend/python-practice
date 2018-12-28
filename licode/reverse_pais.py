class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def mergesort(l, r):
            if l >= r: return 0  # when equals, no contribution to ans and no need to sort
            mid = (l + r) / 2
            ans = mergesort(l, mid) + mergesort(mid + 1, r)  # both inclusive
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]: j += 1
                ans += j - (mid + 1)  # testing case is when j does not move
            nums[l:r + 1] = sorted(nums[l:r + 1])
            return ans

        return mergesort(0, len(nums) - 1)


print Solution().reversePairs([1,3,2,3,1])

