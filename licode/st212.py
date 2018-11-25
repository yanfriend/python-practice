"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
"""


class TrieNode(object):
    def __init__(self):
        self.word=False
        self.children={}


class Solution(object):

    def build_trie(self, words):
        self.trie=TrieNode()

        for word in words:
            curr=self.trie
            for letter in word:
                if curr.children.get(letter) is None:
                    curr.children[letter]=TrieNode()
                curr=curr.children.get(letter)
            curr.word=True

    def dfs(self, board, i, j, visited, ret, path, trie):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return
        if visited[i][j]:
            return

        trie=trie.children.get(board[i][j])
        if trie is None:
            return
        if trie.word:
            ret.add(path+board[i][j])

        visited[i][j]=True
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        for di,dj in dir:
            self.dfs(board, i+di, j+dj, visited, ret, path+board[i][j], trie)
        visited[i][j]=False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.build_trie(words)
        ret=set()
        visited=[[False]*len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,i,j, visited, ret, '', self.trie)
        return list(ret)

# timed out.
# solution: visited from set to array

