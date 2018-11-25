import collections


class Solution(object):
    def replaceWords(self, roots, sentence):
        _trie=lambda: collections.defaultdict(_trie)
        trie=_trie()
        END=True
        for r in roots:
            curr=trie
            for ch in r:
                curr=curr[ch]
            curr[END]=r
        # finish building trie.

        def replace(word):
            curr=trie
            for ch in word:
                curr=curr[ch]
                if END in curr:
                    return curr[END]
            return word

        return ' '.join(map(replace, sentence.split()))

print Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") # the cat was rat by the bat

