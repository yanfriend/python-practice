class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def board_to_str(board):
            return ''.join([str(i) for r in board for i in r])

        moves = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5}, 3: {0, 4}, 4: {1, 3, 5},
                 5: {2, 4}}  # in position 0, switch with pos 1,3
        visited = set()
        cnt = 0
        q = [board_to_str(board)]
        end_board = '123450'

        while q:
            new = []
            for status in q:
                if status == end_board: return cnt
                visited.add(status)

                ind = status.index('0')
                next_arr_org = [s for s in status]
                for m in moves[ind]:
                    next_arr=list(next_arr_org)
                    next_arr[m], next_arr[ind] = next_arr[ind], next_arr[m]
                    next_status = ''.join(next_arr)
                    if next_status not in visited:
                        new.append(next_status)
            q = new
            cnt+=1
        return -1

print Solution().slidingPuzzle([[1,2,3],[4,0,5]])
