"""
Problem Description:

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of words from the dictionary, wherewords are sorted lexicographically
by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
import collections


class Solution(object):
    def alienOrder(self, words):
        if not words: return []
        edges=collections.defaultdict(set) # 'a'->'b'
        indegree=collections.defaultdict(int) # 'a'->2
        for i in range(1,len(words)):
            for j in range(min(len(words[i]),len(words[i-1]))):
                if words[i][j]==words[i-1][j]: continue
                edges[words[i-1][j]].add(words[i][j]);
                indegree[words[i][j]]+=1
                break
        ret=[]
        visited=set()
        char_set=set(''.join(words))
        for ch in char_set:
            if indegree[ch]==0 and ch in edges:
                self.dfs(ret,edges,char_set,ch,visited)

        # check if cycle
        if len(ret)<len(char_set): return []

        return ''.join(ret[::-1])

    def dfs(self,ret,edges,char_set,ch,visited):
        if ch in visited: return
        if ch not in char_set: return
        visited.add(ch)
        for v in edges[ch]:
            self.dfs(ret,edges,char_set,v,visited)
        # ret.insert(0,ch)
        ret.append(ch)

    # another way check cycle, in dfs, add root and change visited to dict,
    # if each node's root is same, then cycle.

print Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) # wertf
print Solution().alienOrder(["baa", "abcd", "abca", "cab", "cad"]) # bdac
print Solution().alienOrder(["caa", "aaa", "aab"]) # cab
