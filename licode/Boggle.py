import collections

Trie = lambda:collections.defaultdict(Trie)
is_word=1

class Boggle(object):
    def __init__(self, board, dictionary):
        self.board=board; self.dictionary=dictionary

        self.trie=Trie()
        for word in dictionary:
            tmp_trie=self.trie
            for ch in word:
                tmp_trie=tmp_trie[ch]
                tmp_trie[is_word]=False
            tmp_trie[is_word]=True
        # have built trie

        self.m=len(self.board)
        self.n=len(self.board[0])

    def findwords(self,x,y):
        """
        find indices of matching words from a point
        """
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def helper(trie, x, y, indices, allindices):
            if not (0 <= x < self.m and 0 <= y < self.n) or board[x][y] == '#': return
            if trie[board[x][y]] is None: return  # not in dict trie

            ch = board[x][y]
            trie=trie[ch]
            indices.append((x,y))
            if trie[is_word]:
                allindices.append(list(indices))

            board[x][y]='#'
            for d in dirs:
                dx,dy=x+d[0],y+d[1]
                helper(trie,dx,dy,indices,allindices)

            board[x][y] =ch
            indices.pop()

        allindices = []
        indices = []
        helper(self.trie, x, y, indices, allindices)
        return allindices

    def findMostStr(self):
        """
        initial function to be called
        :rtype list of string
        :param dict: set of string
        """

        def dfs(pos):
            if pos >= self.m * self.n: return []
            maxres=[]

            for p in range(pos,self.m*self.n):
                x, y = p / self.n, p % self.n
                allindices = self.findwords(x, y)
                for indices in allindices:
                    wlist=[]
                    for i, j in indices:
                        wlist.append(board[i][j])
                        board[i][j] = '#'

                    res=dfs(pos+1)
                    if len(res)+1>len(maxres):
                        maxres = res+[''.join(wlist)]

                    # restore
                    for k,ch in enumerate(wlist):
                        i,j=indices[k]
                        board[i][j]=ch
            return maxres

        return dfs(0)


# board=[
#     ['o','a','t','h'],
#     ['e','t','a','e'],
#     ['i','h','k','r'],
#     ['i','f','l','v'],
# ]
# dictionary=set(["oath","eat","pea","rain"])
# print Boggle(board,dictionary).findMostStr()  # expect: oath, eat


# words=["ab","ac","acd","c","d"]
# dictionary=set(words)
# board=["ab","cd","ab","cd"]
# board=[[c for c in row] for row in board]
# print Boggle(board, dictionary).findMostStr() # ['d', 'c', 'ab', 'd', 'c', 'ab']

board=['abc','def','ghi']
board=[[c for c in row] for row in board]
dictionary = set(["abc", "cfi", "beh", "defi", "gh"])
print Boggle(board,dictionary).findMostStr() # ['gh', 'defi', 'abc']
