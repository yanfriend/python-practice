import Queue

class Node(object):
    def __init__(self, node, parent=None):
        self.node=node
        self.parent=parent


def ten_wizard(wizards):
    def print_path(node):
        ret=[]
        while node is not None:
            ret.append(node.node)
            node=node.parent
        print ret[::-1]

    pq = Queue.PriorityQueue()
    pq.put((0, Node(0)))  # cost 0, node 0
    visited=set()
    target = 9

    while pq.qsize() > 0:
        cost, node = pq.get()
        if node.node == target: print_path(node); return cost

        visited.add(node.node)
        for nei in wizards.get(node.node, []):
            if nei in visited:
                continue
            pq.put((cost + (nei - node.node) ** 2, Node(nei,node)))

    return -1


# test 1
print ten_wizard({0: [1, 4, 5], 4: [9], 1: [0], 9: [4]})  # 41

# test 2
wizards = {0: [1, 5, 9],
           1: [2, 3, 5],
           2: [4],
           5: [9]}
print ten_wizard(wizards)
