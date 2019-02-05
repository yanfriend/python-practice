import collections


class Graph(object):
    def __init__(self, vertexes):
        self.graph=collections.defaultdict(set)
        for vs in vertexes:
            self.graph[vs[0]].add(vs[1])  # error 1, used =, should be add for set

    def min_points(self):
        visited=set()
        topo_path = []

        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nei in self.graph[node]:
                dfs(nei)
            topo_path.append(node)  # reverse to right order

        for node in self.graph.keys():
            dfs(node)

        visited=set()
        ans=[]
        for node in topo_path[::-1]:
            if node not in visited:
                dfs(node)
                ans.append(node)
        return ans


print Graph('AB BA CD DC AC'.split()).min_points() # 1 node, A
print Graph('AB BC CD DA AE FB DG'.split()).min_points()  # 1 node, F
print Graph('AB BC CD DE'.split()).min_points()  # 1 node , A
# #
print Graph('AB BC CA BD DE EF FD'.split()).min_points() # abc (bd) def . 1 node, A
print Graph('AB CB'.split()).min_points()  # 2 nodes, CA
