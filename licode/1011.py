class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            # import ipdb; ipdb.set_trace()
            days = 1 # note:
            current_weight = 0
            for w in weights:
                # current_weight += w
                if current_weight+w > mid:
                    current_weight = 0
                    days += 1
                current_weight += w

            if days > D:
                l = mid + 1
            else:
                r = mid
        return l

print(Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))

