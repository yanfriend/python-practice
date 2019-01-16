from Queue import PriorityQueue

class Node(object):
    def __init__(self, val, parent=None):
        self.val=val
        self.parent=parent

class Solution(object):
    def min_distance(self, wizards, source, target):
        q = PriorityQueue()

        q.put((0, Node(source)))  # distance, Node of id, parent_node_id

        def print_path(node):
            ret = []
            while node != None:
                ret.append(node.val)
                node = node.parent
            print ret[::-1]

        while q.qsize() > 0:
            distance, node = q.get()
            if node.val == target: print_path(node); return distance

            for i, nei in enumerate(wizards[node.val]):
                q.put((distance + (nei - node.val) ** 2, Node(nei, node)))

        return -1

# note: two ways to keep path.


wizards = [
    [1, 5, 9],
    [2, 3, 5],
    [4],
    [],
    [],
    [9],
    [],
    [],
    [],
    []
]

print Solution().min_distance(wizards, 0, 9) # 33
# 0->9(81), or 0->5->9(25+16<81), 0->1->5->9 (16+16+1=33)
