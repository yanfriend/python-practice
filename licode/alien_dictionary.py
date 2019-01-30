
class Solution(object):
    def alienOrder(self, dictionary):
        char_set=set(ch for word in dictionary for ch in word )
        graph={}
        indegree={}
        for ch in char_set:
            graph[ch] = set()
            indegree[ch] = 0

        for i in range(1, len(dictionary)):
            for j in range(min(len(dictionary[i]), len(dictionary[i-1]))):
                if dictionary[i][j] == dictionary[i-1][j]: continue
                graph[dictionary[i-1][j]].add(dictionary[i][j]); break # error 1, miss break

        for node in graph: # error 2, mix indegree calculate together
            for nei in graph[node]:
                indegree[nei]+=1

        zero_in_degree = [ch for ch in indegree if indegree[ch]==0]

        def topo_single(zero_in_degree):
            ret=list(zero_in_degree)

            qu=zero_in_degree
            while len(qu)>0:
                new=[]
                for node in qu:
                    for nei in graph[node]:
                        indegree[nei]-=1
                        if indegree[nei]==0:
                            ret.append(nei)
                            new.append(nei)
                qu=new
            return ret

        def topo_all(ret, zero_in_degree, path, visited): # my another one is better
            if len(path)==len(graph): ret.append(path); return

            qu=list(zero_in_degree)
            for node in qu:
                if node in visited: continue
                visited.add(node)

                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        zero_in_degree.append(nei)

                topo_all(ret, zero_in_degree, path+node, visited)

                for nei in graph[node]:
                    if indegree[nei] == 0:
                        zero_in_degree.remove(nei)
                    indegree[nei] += 1
                visited.remove(node)

        ret = topo_single(zero_in_degree)
        if len(ret)==len(char_set): return ret
        else: return []

        # ret=[]
        # visited=set()
        # topo_all(ret,zero_in_degree, '', visited)
        # return ret



print Solution().alienOrder(["wrt","wrf","er","ett","rftt"]) # wertf
print Solution().alienOrder(["baa", "abcd", "abca", "cab", "cad"]) # bdac

print Solution().alienOrder(["caa", "aaa", "aab"]) # cab

print Solution().alienOrder(["aaf", "ab"]) # fab, or abf, afb
print Solution().alienOrder(["aaf", "ab", 'fg']) # fab, or abc, afb

print Solution().alienOrder(["ba", "aa", "ab"]) # empty b->a, a->b
