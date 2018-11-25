class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret=[]
        m=len(matrix) if matrix else 0
        n=len(matrix[0]) if m else 0

        cnt=0
        start_row=0; end_row=m-1
        start_col=0; end_col=n-1

        while len(ret)<m*n:
            j=start_col
            while j<=end_col:
                ret.append(matrix[start_row][j])
                j+=1
            start_row+=1

            i=start_row
            while i<=end_row:
                ret.append(matrix[i][end_col])
                i+=1
            end_col-=1

            import ipdb;ipdb.set_trace()

            j=end_col
            # need if about end_row and start_row
            while j>=start_col:
                ret.append(matrix[end_row][j])
                j-=1
            end_row-=1

            i=end_row
            while i>=start_row:
                ret.append(matrix[i][start_col])
                i-=1
            start_col+=1

        return ret

print Solution().spiralOrder([[2,3]])
