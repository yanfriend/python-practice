import collections

Trie = lambda : collections.defaultdict(Trie)
IS_WORD=1

class Boggle(object):
    def __init__(self, board, dictionary):
        m=len(board)
        n=len(board[0])
        self.board=[['']*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.board[i][j]=board[i][j]

        self.trie=Trie()
        for word in dictionary:
            tmp=self.trie
            for ch in word:
                tmp=tmp[ch]
            tmp[IS_WORD]=True

    def findMostStr(self):
        m = len(self.board)
        n = len(self.board[0])

        def find_words(ret, trie, i,j, path): # find all word from i,j
            if i<0 or j<0 or i>=m or j>=n: return

            char=self.board[i][j]
            if char not in trie: return

            path.append((i,j))
            if trie[char][IS_WORD]:
                ret.append(list(path))

            self.board[i][j]='#'
            delta=((i,j+1),(i,j-1),(i+1,j),(i-1,j))
            for dx,dy in delta:
                find_words(ret,trie[char], dx, dy, path)
            self.board[i][j]=char

        def helper(pos):
            if pos>=m*n: return []
            i = pos / n  # error, divide column
            j = pos % n

            max_ret=helper(pos+1)

            words_ind = []
            find_words(words_ind, self.trie, i, j, [])
            for wind in words_ind:
                word=[]
                for ind in wind:
                    word.append(self.board[ind[0]][ind[1]])
                    self.board[ind[0]][ind[1]] = '#'

                # call next
                ret=helper(pos+1)

                ret.append(''.join(word))
                if len(ret)>len(max_ret):
                    max_ret=list(ret)

                # resume board
                for i in range(len(word)):
                    self.board[wind[i][0]][wind[i][1]] = word[i]

            return max_ret

        return helper(0)


# board=['abc','def','ghi']
# dictionary = set(["abc", "cfi", "beh", "defi", "gh", "abcf"])
# print Boggle(board,dictionary).findMostStr() # ['gh', 'defi', 'abc']
#
# board=[ 'oath', 'etae', 'ihkr','iflv']
# dictionary=set(["oath","eat","pea","rain"])
# print Boggle(board,dictionary).findMostStr()  # expect: oath, eat


words=["ab","ac","acd","c","d"]
dictionary=set(words)
board=["ab","cd","ab","cd"]
print Boggle(board, dictionary).findMostStr() # ['d', 'c', 'ab', 'd', 'c', 'ab']
