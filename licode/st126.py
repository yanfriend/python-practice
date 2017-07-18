"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
import string

class WordNode(object):
    def __init__(self,pre,word):
        self.pre=pre
        self.word=word

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        qu=[WordNode(None,beginWord)]
        ret=[]
        word_set=set(wordList)
        word_set.add(beginWord) # add begin word to continue
        visited=set()

        while qu:
            next_qu=[]
            for word_node in qu:
                word=word_node.word
                if word in word_set:
                    if word==endWord:
                        path=[]
                        while word_node:
                            path.append(word_node.word)
                            word_node=word_node.pre
                        ret.append(path[::-1]) # revsered() returns iterator, use list!
                        continue

                    visited.add(word)

                    for i in range(len(word)):
                        for ch in string.lowercase:
                            new_word=word[:i]+ch+word[i+1:]
                            if new_word in word_set: # opt 2
                                next_qu.append(WordNode(word_node,new_word))

            if ret: return ret
            qu=next_qu
            word_set-=visited
            visited.clear()
        return []

# print Solution().findLadders('a','c',['a','b','c'])
print Solution().findLadders('hit','cog',["hot","dot","dog","lot","log","cog"])
