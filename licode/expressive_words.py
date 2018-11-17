class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0

        def word_count(s):
            letter = [s[0]];
            cnt = [1]
            for i in range(1, len(s)):
                if s[i] == letter[-1]:
                    cnt[-1] += 1
                else:
                    letter.append(s[i]); cnt.append(1)
            return letter, cnt

        l1, cnt1 = word_count(S)

        for w in words:
            l2, cnt2 = word_count(w)
            if len(l1) != len(l2): continue
            expressive = True
            for i in range(len(cnt1)):
                if l1[i] != l2[i]: expressive = False; break
                if cnt1[i] == cnt2[i] or cnt1[i] >= max(3, cnt2[i]):
                    continue
                else:
                    expressive = False; break
            if expressive: ans += 1
        return ans


print Solution().expressiveWords("dddiiiinnssssssoooo",
["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"])

