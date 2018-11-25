class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        import collections
        cut_first = collections.defaultdict(list)
        for w in words:
            cut_first[w[0]].append(w[1:])

        ans = 0
        for s in S:
            left = cut_first.pop(s, ())
            for l in left:
                if not l: ans += 1; continue
                cut_first[left[0]].append(left[1:])
        return ans

print Solution().numMatchingSubseq("dsahjpjauf",
["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])
