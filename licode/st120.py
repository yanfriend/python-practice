"""

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # use triangle itself for store, and bottom up to get the minimal value directly.

        row_len=len(triangle)
        for i in range(row_len-1,0,-1):
            for j in range(len(triangle[i])-1):
                triangle[i-1][j]+=min(triangle[i][j],triangle[i][j+1])

        return triangle[0][0]
