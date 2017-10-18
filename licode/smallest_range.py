import Queue

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq=Queue.PriorityQueue()
        max_val=float('-inf')
        min_range=float('inf')
        ret=[]

        for i in range(len(nums)):
            pq.put((nums[i][0],i,0))
            max_val=max(max_val,nums[i][0])

        while True:
            tmp_min,tmp_i,tmp_j=pq.get()
            tmp_range=max_val-tmp_min
            if tmp_range<min_range:
                min_range=tmp_range
                ret=[tmp_min,max_val]
            if tmp_j>=len(nums[tmp_i])-1: break
            pq.put((nums[tmp_i][tmp_j+1],tmp_i,tmp_j+1))
            max_val=max(max_val,nums[tmp_i][tmp_j+1])

        return ret

print Solution().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])

