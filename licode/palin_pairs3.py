def palin_pairs(inp):
    mp = {}
    for i, w in enumerate(inp):
        mp[w] = i

    ret = []

    def is_palin(s):
        return s == s[::-1]

    for i, w in enumerate(inp):
        for j in range(len(w) + 1):
            left = w[:j][::-1]
            right = w[j:][::-1]
            if left in mp and mp[left] != i and is_palin(right) and j != len(w):
                ret.append([i, mp[left]])
            if right in mp and mp[right] != i and is_palin(left):
                ret.append([mp[right], i])
    return ret


# print palin_pairs(['abb', 'a', 'b'])  # [[0, 1]]
#
print palin_pairs(['abc', 'cba', 'b'])  # [[1, 0], [0, 1]] # this is why j!=len(w) to avoid dup

# print palin_pairs(['abba', '', 'b'])  # [[0, 1], [1, 0], [2, 1], [1, 2]]


# # below from previous
# print palin_pairs(['abb','bba','a', 'aba']) # [(1, 0), (0, 2), (0, 1), (2, 1)]
#
print palin_pairs(["a",""]) # [(0, 1), (1, 0)] # this is for j to len(w)
#
# print palin_pairs(["abcd","dcba","lls","s","sssll"]) # [(1, 0), (0, 1), (3, 2), (2, 4)]
