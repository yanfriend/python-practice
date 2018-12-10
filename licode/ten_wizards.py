from Queue import PriorityQueue


class Solution(object):

    def min_distance(self, wizards, source, target):
        q = PriorityQueue()
        parents = [0] * len(wizards)

        q.put((0, source, [source]))  # distance, id, parent_node_id

        def print_return():
            id = target
            ans = []
            while id != source:
                ans.append(id)
                id = parents[id]
            ans.append(source)
            print list(reversed(ans))

        while q.qsize() > 0:
            distance, id, parent_id = q.get()

            if id == target: print parent_id; print_return(); return distance

            for i, node in enumerate(wizards[id]):
                parents[node] = id
                q.put((distance + (id - node) ** 2, node, parent_id + [node]))

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

print Solution().min_distance(wizards, 0, 9)
# 0->9(81), or 0->5->9(25+16<81), 0->1->5->9 (16+16+1=33)
