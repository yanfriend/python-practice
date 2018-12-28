class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words.sort(key=len)
        ans = []
        words_set = set()

        for w in words:
            dp = [False] * (len(w) + 1);
            dp[0] = True  # why +1 dp? cos we need when length is 0
            if len(w) == 0: dp[0] = False

            for i in range(len(w) + 1):
                for j in range(i):
                    if dp[j] and w[j:i] in words_set:
                        # if whole w in set, dp is True even 1 subword.
                        # but will not happen to i cos w is not added yet.
                        dp[i] = True;
                        break
            if dp[len(w)]:
                ans.append(w)
            words_set.add(w)  # tricky 2, w was not in set when dp-ing.
        return ans

print Solution().findAllConcatenatedWordsInADict(["a","b","ab"])
# print Solution().findAllConcatenatedWordsInADict(['aa', 'b', 'aabc',]) #  'c', 'd'])
# print Solution().findAllConcatenatedWordsInADict(
#     ["cat","cats","catsdogcats","dog"]) # ,"dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
