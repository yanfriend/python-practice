import collections

Trie = lambda : collections.defaultdict(Trie)
is_word = 1

class Boggle(object):
    def __init__(self, board, dictionary):
        self.trie = self.build_trie(dictionary)
        board = [[c for c in row] for row in board]
        self.board=board

    def build_trie(self, dictionary):
        trie=Trie()
        for w in dictionary:
            curr=trie
            for letter in w:
                curr=curr[letter]
            curr[is_word]=True
        return trie

    def findMostStr(self):
        m=len(self.board); n=len(self.board[0])

        def find_all_words(row, col):
            ret=[]
            visited=set()
            trie=self.trie

            def word_dfs(row, col, trie, path):
                char = self.board[row][col]
                if char not in trie: return

                if trie[char][is_word]:
                    ret.append(path+[(row,col)])

                for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr,nc=row+dx,col+dy
                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        word_dfs(nr,nc, trie[char],path+[(row,col)])
                        visited.remove((nr,nc))

            word_dfs(row, col,trie, [])
            return ret

        def board_dfs(pos):
            if pos>=m*n: return
            max_ret = [] # note: try not to use global for writing, everywhere

            for p in range(pos, m*n):
                row=p/n; col=p%n
                words = find_all_words(row, col)

                for w_indices in words:
                    # set char to #, continue board_dfs in new pos.
                    word=''
                    for i, j in w_indices:
                        word += self.board[i][j]
                        # w_keep[(i,j)]=self.board[i][j]
                        self.board[i][j]='#'

                    curr_maxret = board_dfs(pos+1) # note, here is pos

                    for ind, (i, j) in enumerate(w_indices):
                        self.board[i][j] = word[ind]

                    if len(curr_maxret)+1>len(max_ret):
                        max_ret=curr_maxret+[word]

            return max_ret

        return board_dfs(0)




board=['abc','def','ghi']
dictionary = set(["abc", "cfi", "beh", "defi", "gh", "abcf"])
print Boggle(board,dictionary).findMostStr() # ['gh', 'defi', 'abc']

board=[ 'oath', 'etae', 'ihkr','iflv']
dictionary=set(["oath","eat","pea","rain"])
print Boggle(board,dictionary).findMostStr()  # expect: oath, eat


words=["ab","ac","acd","c","d"]
dictionary=set(words)
board=["ab","cd","ab","cd"]
print Boggle(board, dictionary).findMostStr() # ['d', 'c', 'ab', 'd', 'c', 'ab']
