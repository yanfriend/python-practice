class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False

        parents = dict()
        for w in words1: parents[w] = w
        for w in words2: parents[w] = w

        for p in pairs:
            parents[p[0]] = p[1]

        for i in range(len(words1)):
            if self.find_parent(parents, words1[i]) != self.find_parent(parents, words2[i]): return False

        return True

    def find_parent(self, parents, p):
        if p not in parents: parents[p] = p

        if parents[p] == p: return p
        parents[p] = self.find_parent(parents, parents[p])
        return parents[p]


print Solution().areSentencesSimilarTwo(["great", "acting", "skills"],
                                        ["fine", "drama", "talent"],
                                        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]])  # true

print Solution().areSentencesSimilarTwo(["great", "acting", "skills"],
                                        ["fine", "drama", "talent"],
                                        [["great", "good"], ["fine", "good"], ["acting", "drama"],
                                         ["skills", "talent"]])  # True
