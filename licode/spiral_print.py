class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        r1 = c1 = 0
        r2 = m - 1;
        c2 = n - 1
        ans = []

        def fill_cycle(r1, c1, r2, c2):
            if r1 == r2:
                for c in range(c1, c2 + 1): ans.append(matrix[r1][c])
            elif c1 == c2:
                for r in range(r1, r2 + 1): ans.apppend(matrix[r][c1])
            else:
                for c in range(c1, c2 + 1): ans.append(matrix[r1][c])
                for r in range(r1 + 1, r2 + 1): ans.append(matrix[r][c2])
                for c in range(c2 - 1, c1 - 1, -1): ans.append(matrix[r2][c])
                for r in range(r2 - 1, r1, -1): ans.append(matrix[r][c1])

        while r1 <= r2 and c1 <= c2:
            fill_cycle(r1, c1, r2, c2)
            r1 += 1;
            r2 -= 1;
            c1 += 1;
            c2 -= 1
        return ans

print Solution().spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])