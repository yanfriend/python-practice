import collections

Trie = lambda: collections.defaultdict(Trie)
IS_WORD = 1


class Boggle4(object):
    def __init__(self, board, dictionary):
        self.board = [[''] * len(board[0]) for _ in range(len(board))]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = board[i][j]

        self.trie = Trie()
        for word in dictionary:
            tmp = self.trie
            for ch in word:
                tmp = tmp[ch]
            tmp[IS_WORD] = True

    def findMostStr(self):
        m = len(self.board)
        n = len(self.board[0])

        def find_words(ret, trie, path, row, col):
            if not (0 <= row < m and 0 <= col < n):
                return
            ch = self.board[row][col]
            if ch not in trie:
                return

            trie = trie[ch]
            if trie[IS_WORD]:
                ret.append(path + [(row, col)])

            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            self.board[row][col] = '#'
            for dx, dy in dirs:
                newx, newy = row + dx, col + dy
                find_words(ret, trie, path + [(row, col)], newx, newy)
            self.board[row][col] = ch

        def helper(pos):
            if pos > m * n: return []
            row = pos / n
            col = pos % n

            words_ind = []
            find_words(words_ind, self.trie, [], row, col)
            ret_max = helper(pos + 1)

            for wind in words_ind:
                letters = ''
                for i, j in wind:
                    letters += self.board[i][j]
                    self.board[i][j] = '#'

                curr_ret = helper(pos + 1)
                curr_ret.append(letters)
                if len(curr_ret) > len(ret_max):
                    ret_max = curr_ret

                for wind, (i, j) in enumerate(wind):
                    self.board[i][j] = letters[wind]
            return ret_max

        return helper(0)


words=["ab","ac","bd", "ad"]
dictionary=set(words)
board=["ab","cd",]
print Boggle4(board, dictionary).findMostStr() # ['bd', 'ac'], simplest one for testing



board=['abc','def','ghi']
dictionary = set(["abc", "cfi", "beh", "defi", "gh", "abcf"])
print Boggle4(board,dictionary).findMostStr() # ['gh', 'defi', 'abc']

board=[ 'oath', 'etae', 'ihkr','iflv']
dictionary=set(["oath","eat","pea","rain"])
print Boggle4(board,dictionary).findMostStr()  # expect: oath, eat

words=["ab","ac","acd","c","d"]
dictionary=set(words)
board=["ab","cd","ab","cd"]
print Boggle4(board, dictionary).findMostStr() # ['d', 'c', 'ab', 'd', 'c', 'ab']
