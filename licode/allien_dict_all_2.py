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

        for k, v in indegree.items():
            if v == 0 and k not in visited:
                visited.add(k)
                for nei in graph[k]:
                    indegree[nei] -= 1

                self.topological_sort(graph, indegree, ret, path + k, visited)

                for nei in graph[k]:
                    indegree[nei] += 1
                visited.remove(k)


print Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) # wertf
print Solution().alienOrder(["baa", "abcd", "abca", "cab", "cad"]) # bdac
print Solution().alienOrder(["caa", "aaa", "aab"]) # cab

print Solution().alienOrder(["aaf", "ab"]) # fab, or abc, afb
print Solution().alienOrder(["aaf", "ab", 'fg']) # ['abgf', 'abfg', 'agbf', 'agfb', 'afbg', 'afgb', 'gabf', 'gafb']

print Solution().alienOrder(["ba", "aa", "ab"]) # empty b->a, a->b
