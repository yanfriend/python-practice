
import collections

Trie = lambda : collections.defaultdict(Trie)
IS_WORD=True


def k_distance(words, target, k):
    trie=Trie()
    for word in words:
        tmp=trie
        for ch in word:
            tmp=tmp[ch] # error 1, used trie instead tmp after =
        tmp[IS_WORD] = True

    dist=[i for i in range(len(target)+1)]
    ret=[]

    def helper(trie, path, dist):
        if trie[IS_WORD]:
            if dist[-1]<=k:
                ret.append(path)
            else:
                return

        for ch in trie:
            if ch==IS_WORD: continue

            new_dist=[i for i in range(len(target)+1)]  # error 2: messed up original dp
            new_dist[0]=len(path)+1

            for j in range(1,len(target)+1): # populate the new row!
                if target[j-1]==ch:
                    new_dist[j] = dist[j-1] # like previous row, j-1
                else:
                    new_dist[j] = min(new_dist[j-1], dist[j-1], dist[j])+1 # corresponding to add/delete/replace a char
            helper(trie[ch], path+ch, new_dist)

    helper(trie, '', dist)
    return ret


print k_distance(["ad", "c", "cc"], 'abcd', 2)  # ['ad']

print k_distance(["abcd", "abc", "abd", "ad", "c", "cc"], 'abcd', 2)  # ['abcd', 'abc', 'abd', 'ad']
