class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        https://blog.csdn.net/zjucor/article/details/79315716
        """
        N = len(board)
        import collections
        cnt = collections.Counter(tuple(b) for b in board)

        if len(cnt) != 2: return -1  # only allow two types of rows.

        for a, b in zip(*cnt.keys()):  # 1-0 or 0-1; cant be 1-1, or 0-0.
            # * to unpack the list, so *['11','01'] becomes '11', '01'
            if a == b: return -1

        col = sum(board[0][i] == i & 1 for i in range(N))  # row 0, all col, how many 1's
        row = sum(board[i][0] == i & 1 for i in range(N))  # col 0, how many 1's

        if N % 2:
            for i in cnt:
                if sum(i) not in [N // 2, N // 2 + 1] or cnt[i] not in [N // 2, N // 2 + 1]: return -1
            if col & 1: col = N - col  # col is odd, col is larger than N-col
            if row & 1: row = N - row
        else:
            for i in cnt:
                if sum(i) != N / 2 or cnt[i] != N / 2: return -1 # number of 1's in it, and tuple appear times
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) // 2

print Solution().movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]) # 2


