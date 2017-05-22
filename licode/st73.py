class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row0=any(num==0 for num in matrix[0])
        col0=any(matrix[i][0]==0 for i in range(len(matrix)))

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=matrix[i][0]=0

        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j]=0

        for j in range(1,len(matrix[0])):
            if matrix[0][j]==0:
                for i in range(1,len(matrix)):
                    matrix[i][j]=0

        if row0:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if col0:
            for i in range(len(matrix)):
                matrix[i][0]=0

matrix=[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
Solution().setZeroes(matrix)
print matrix

