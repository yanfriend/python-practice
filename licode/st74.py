class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0]) if m else 0

        i=0;j=n-1
        while 0<=i<m and 0<=j<n:
            import ipdb; ipdb.set_trace()

            if matrix[i][j]>target:
                j-=1
            elif matrix[i][j]<target:
                i+=1
            else:
                return True
        return False

# print Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
print Solution().searchMatrix([],0)
