class Node(object):
    def __init__(self, status, parent=None):
        self.status=status
        self.parent=parent


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        def board_to_str(board):
            return ''.join([str(i) for r in board for i in r])

        def print_path(node):
            ret=[]
            while node is not None:
                ret.append(node.status)
                node=node.parent
            ret=ret[::-1]
            print ret

        moves = {0: {1, 3}, 1: {0, 2, 4}, 2: {1, 5},
                 3: {0, 4, 6}, 4: {1, 3, 5, 7}, 5: {2, 4, 8},
                 6: {3,7}, 7: {4,6,8}, 8:{5,7}
                 }  # in position 0, switch with pos 1,3
        visited = set()
        cnt = 0
        q = [Node(board_to_str(board))]
        end_board = '123456780'

        while q:
            new = []
            for node in q:
                if node.status == end_board: print_path(node); return cnt
                visited.add(node.status)

                ind = node.status.index('0')
                next_arr_org = [s for s in node.status]
                for m in moves[ind]:
                    next_arr=list(next_arr_org)
                    next_arr[m], next_arr[ind] = next_arr[ind], next_arr[m]
                    next_status = ''.join(next_arr)
                    if next_status not in visited:
                        new.append(Node(next_status,node))
            q = new
            cnt+=1
        return -1


print Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5], [6, 7, 8]]) # 14

print Solution().slidingPuzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]]) # 2


print Solution().slidingPuzzle([[0,2,1],[8,3,5],[6,7,4]])  # -1