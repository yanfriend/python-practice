import collections

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret=[[float('inf')]*len(matrix[0]) for _ in range(len(matrix))]
        visited={}

        def bfs(i, j):
            if (i,j) in visited:
                return ret[i][j]

            deque=collections.deque()


            return ret[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    ret[i][j]=0
                else:
                    bfs(i, j)
        return ret

print Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])

