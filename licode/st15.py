class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        ret=[]

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            j=i+1; k=len(nums)-1
            while j<k:
                if j-1>i and nums[j]==nums[j-1]: j+=1;continue
                if k<len(nums)-1 and nums[k]==nums[k+1]: k-=1;continue

                ss=nums[i]+nums[j]+nums[k]
                if ss==0:
                    ret.append([nums[i],nums[j],nums[k]])
                    k-=1; j+=1
                elif ss>0:
                    k-=1
                else:
                    j+=1
        return ret


'''
Total Accepted: 211384
Total Submissions: 982437
Difficulty: Medium
Contributor: LeetCode
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Subscribe to see which companies asked this question.
'''
