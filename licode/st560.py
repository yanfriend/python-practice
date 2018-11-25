
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter=collections.Counter()
        counter[0]=1

        pre_sum=0
        cnt=0
        for num in nums:
            pre_sum+=num
            cnt += counter[pre_sum-k]
            counter[pre_sum]+=1
        return cnt



