import collections

Trie = lambda: collections.defaultdict(Trie)
is_word = 1


def k_distance(words, target, k):
    # build trie
    trie = Trie()
    for w in words:
        tmp = trie
        for ch in w:
            tmp = tmp[ch]
        tmp[is_word] = True

    def helper(path, trie, prev_dist):
        if trie[is_word]:
            if prev_dist[-1] <= k:
                ret.append(path)
            else:
                return
        for char in trie:
            if char == 1: continue  # skip is_word
            curr_dist = [i for i in range(len(target) + 1)]
            curr_dist[0] = len(path) + 1  # why +1 ? path should add char now.
            for j in range(1, len(prev_dist)):
                if target[j - 1] == char:
                    curr_dist[j] = prev_dist[j - 1]  # like previous row i.e. (row-1), col-1
                else:
                    curr_dist[j] = min(curr_dist[j - 1], prev_dist[j], prev_dist[j - 1]) + 1
            helper(path + char, trie[char], curr_dist)

    ret = []
    dist = [i for i in range(len(target) + 1)]
    helper('', trie, dist)
    return ret


print k_distance(["ad", "c", "cc"], 'abcd', 2)  # ['ad']
print k_distance(["abcd", "abc", "abd", "ad", "c", "cc"], 'abcd', 2)  # ['abcd', 'abc', 'abd', 'ad']
