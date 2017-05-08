class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt=collections.defaultdict(int)
        for num in nums:
            cnt[num]+=1

        hp=[]
        for num, count in cnt.iteritems():
            heapq.heappush(hp, (count,num))
            if len(hp)>k:
                heapq.heappop(hp)

        return [num for (_,num) in hp]
