import collections

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        count = collections.Counter()
        for w in words:
            if len(set(w)) > 7: continue
            m = 0
            for c in w:
                m |= 1 << (ord(c) - 97)
            count[m] += 1
        print count

        res = []
        for p in puzzles:
            bfs = [1 << (ord(p[0]) - 97)]
            for c in p[1:]:
                bfs += [m | 1 << (ord(c) - 97) for m in bfs]
            print p, bfs
            res.append(sum(count[m] for m in bfs))
        return res

print Solution().findNumOfValidWords(words=["aaaa","asas","able","ability","actt","actor","access"], \
puzzles=["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])