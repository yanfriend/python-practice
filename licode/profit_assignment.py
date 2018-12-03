class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted([a, b] for a, b in zip(difficulty, profit))
        res = i = maxp = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                maxp = max(jobs[i][1], maxp) # this include the max p under worker capacity
                i += 1
            res += maxp
        return res

print Solution().maxProfitAssignment(
    [1, 5,6],
    [100, 1,1],
    [6,6,6]
)
