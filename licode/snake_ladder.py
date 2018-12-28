class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        def jump(cell):
            row = n - 1 - (cell - 1) / n
            if row % 2 == n % 2:
                col = n - 1 - (cell - 1) % n
            else:
                col = (cell - 1) % n
            if board[row][col] == -1: return cell
            return board[row][col]

        step = 0
        qu = [1]
        visited = set([1])
        while len(qu) > 0:
            new_qu = []
            for start in qu:
                if start == n * n: return step
                for i in range(1, 7):
                    next_start = start + i
                    if not 1 <= next_start <= n * n: continue
                    next_start = jump(next_start)
                    if next_start in visited: continue
                    visited.add(next_start)
                    new_qu.append(next_start)
            qu = new_qu
            step += 1
        return -1


print Solution().snakesAndLadders([
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]])  # 4


print Solution().snakesAndLadders([
    [-1,-1,19,10,-1],
    [2,-1,-1,6,-1],
    [-1,17,-1,19,-1],
    [25,-1,20,-1,-1],
    [-1,-1,-1,-1,15]
 ]) # 2

