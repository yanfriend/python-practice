"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word,0):
                    return True
        return False

    def dfs(self, board, i, j, word, ind):
        if ind>=len(word): return True
        if not (0<=i<len(board) and 0<=j<len(board[0])):
            return False
        if board[i][j]!=word[ind]:
            return False

        tmp=board[i][j]
        board[i][j]='#'
        dir=((1,0),(-1,0),(0,1),(0,-1))
        for di,dj in dir:
            if self.dfs(board,i+di, j+dj, word, ind+1):
                return True
        board[i][j]=tmp
        return False
