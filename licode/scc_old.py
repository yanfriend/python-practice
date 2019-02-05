from collections import defaultdict
from collections import deque


class Graph(object):
    """A directed graph. Nodes may be any hashable values."""

    def __init__(self, edges=()):
        """Initialize graph from optional iterable of edges."""
        self.out_nodes = defaultdict(set) # Map from node to its out-neighbours
        self.in_nodes = defaultdict(set) # Map from node to its in-neighbours
        for u, v in edges:
            self.out_nodes[u].add(v)
            self.in_nodes[v].add(u)

    def components(self):
        """Return list of strongly connected components."""
        visited = set()  # Set of visited nodes.
        L = deque() # Nodes in topological order. can change to deque

        def visit(u):
            if u not in visited:
                visited.add(u)
                for v in self.out_nodes[u]:
                    visit(v)
                L.appendleft(u)

        for u in self.out_nodes.keys():
            visit(u)
        component = defaultdict(set)  # Map from root to its component.
        assigned = set()  # Set of nodes assigned to a component.

        def assign(u, root):
            if u not in assigned:
                component[root].add(u)
                assigned.add(u)
                for v in self.in_nodes[u]: # this is actually reversed graph.
                    assign(v, root)

        for u in L:
            assign(u, u)
        return component  # list(component.values())

    def min_poinst(self):
        comps = self.components()
        ans=0
        for cp in comps.values():
            cnt=0
            for node in cp:
                cnt += len([nei for nei in self.in_nodes[node] if nei not in cp])
            if cnt==0:
                ans+=1
        return ans

print Graph('AB BA CD DC AC'.split()).min_poinst() # 1 node
print Graph('AB BC CD DA AE FB DG'.split()).min_poinst()  # 1 node
print Graph('AB BC CD DE'.split()).min_poinst()  # 1 node
#
# print Graph('AB BC CA BD DE EF FD'.split()).components() # abc (bd) def
print Graph('AB BC CA BD DE EF FD'.split()).min_poinst() # abc (bd) def . 1 node has to be selected.
print Graph('AB CB'.split()).min_poinst()  # 2 nodes
