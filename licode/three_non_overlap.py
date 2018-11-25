"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_left=[(0,0)]*len(nums) # (sum, index)
        max_mid=[0]*len(nums)
        max_right=[(0,0)]*len(nums)

        tmp_sum=0
        for i in range(len(nums)):
            tmp_sum+=nums[i]
            if i>=k-1:
                max_mid[i]=tmp_sum # set max_mid
                tmp_sum-=nums[i-k+1]

        tmp_sum=0
        for i in range(len(nums)):
            tmp_sum+=nums[i]
            if i>=k-1:
                if tmp_sum>max_left[i-1][0]:
                    max_left[i]=(tmp_sum,i-k+1)
                else:
                    max_left[i]=max_left[i-1]
                tmp_sum-=nums[i-k+1]

        tmp_sum=0
        for i in range(len(nums)-1,-1,-1):
            tmp_sum+=nums[i]
            if i<=len(nums)-k:
                if i+1>=len(nums) or tmp_sum>=max_right[i+1][0]:
                    max_right[i]=(tmp_sum,i)
                else:
                    max_right[i]=max_right[i+1]
                tmp_sum-=nums[i+k-1]

        max_val=0
        ret=[]
        for i in range(k-1,len(nums)-k-1):
            tmp_sum=max_left[i][0]+max_mid[i+k]+max_right[i+k+1][0]
            if tmp_sum>max_val:
                max_val=tmp_sum
                ret=[max_left[i][1],i+1,max_right[i+k+1][1]]
        return ret

print Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)  # [0, 3, 5]
print Solution().maxSumOfThreeSubarrays([4,5,10,6,11,17,4,11,1,3],1) # [4,5,7]


'''
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        nsize = size - k + 1
        sums = [0] * nsize
        maxa = [0] * nsize
        maxb = [0] * nsize
        total = 0

        for x in range(size):
            total += nums[x]
            if x >= k - 1:
                sums[x - k + 1] = total
                total -= nums[x - k + 1]

        maxn, maxi = 0, 0
        for x in range(nsize):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxa[x] = (maxn, maxi)

        maxn, maxi = 0, nsize - 1
        for x in range(nsize - 1, -1, -1):
            if sums[x] > maxn:
                maxn, maxi = sums[x], x
            maxb[x] = (maxn, maxi)

        ansn, ansi = 0, None
        for x in range(k, nsize - k):
            va, ia = maxa[x - k]
            vb, ib = maxb[x + k]
            if sums[x] + va + vb > ansn:
                ansn = sums[x] + va + vb
                ansi = [ia, x, ib]
        return ansi
'''
