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

The follow up: print all possible letter orders
"""


class Solution(object):
    def alienOrder(self, words):
        if not words: return []

        char_set = set(''.join(words))
        graph = {}
        indegree = {}  # 'a'->2
        for c in char_set:  # this is needed as may miss isolated chars
            graph[c] = set()
            indegree[c] = 0

        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i][j] == words[i - 1][j]: continue
                graph[words[i - 1][j]].add(words[i][j]);
                indegree[words[i][j]] += 1
                break

        ret = []
        visited = set()
        self.topological_sort(graph, indegree, ret, '', visited)
        return ret

    def topological_sort(self, graph, indegree, ret, path, visited):
        if len(visited) == len(graph):
            ret.append(path)
            return

        qu = [k for k, v in indegree.items() if v==0]

        for q in qu:
            if q in visited: continue
            visited.add(q)
            for nei in graph[q]:
                indegree[nei] -= 1
            self.topological_sort(graph, indegree, ret, path + q, visited)
            visited.remove(q)
            for nei in graph[q]:
                indegree[nei] += 1


print Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) # wertf
print Solution().alienOrder(["baa", "abcd", "abca", "cab", "cad"]) # bdac
print Solution().alienOrder(["caa", "aaa", "aab"]) # cab

print Solution().alienOrder(["aaf", "ab"]) # fab, or abc, afb
print Solution().alienOrder(["aaf", "ab", 'fg']) # ['abgf', 'abfg', 'agbf', 'agfb', 'afbg', 'afgb', 'gabf', 'gafb']

print Solution().alienOrder(["ba", "aa", "ab"]) # empty b->a, a->b
