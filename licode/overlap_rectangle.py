def overlap_rectangle(rects):
    def overlap(rec1, rec2):
        return rec1[1][0] > rec2[0][0] and rec1[0][0] < rec2[1][0] and \
               rec1[1][1] > rec2[0][1] and rec1[0][1] < rec2[1][1]

    parent = [i for i in range(len(rects))]

    def find_parent(i):
        if i != parent[i]:  # error1, used while
            parent[i] = find_parent(parent[i])
        return parent[i]

    def union(i, j):
        pi = find_parent(i)
        pj = find_parent(j)
        if pi != pj:
            parent[pi] = pj

    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            if overlap(rects[i], rects[j]):
                union(i, j)

    s = set([find_parent(i) for i in range(len(rects))])  # error 2, used wrong way to find all parents
    return len(s)


rectangles = [
    [[0, 0], [4, 4]],
    [[1, 2], [3, 5]],
    [[1, 1], [3, 3]],
    [[6, 6], [7, 7]]
]
print overlap_rectangle(rectangles)
