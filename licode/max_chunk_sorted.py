class Solution:
  def maxChunksToSorted(self, arr):
    v = sorted([(n,i) for i, n in enumerate(arr)])
    m = 0
    ans = 0
    for i, n in enumerate(v):
      m = max(m, n[1])
      if i == m: ans += 1
    return ans


    # v = sorted([(n << 32) | i for i, n in enumerate(arr)])
    # m = 0
    # ans = 0
    # for i, n in enumerate(v):
    #   m = max(m, n & 0xffffffff)
    #   if i == m: ans += 1
    # return ans

print Solution().maxChunksToSorted([2,1,3,4,4])
print Solution().maxChunksToSorted([2,3,5,4,4])
