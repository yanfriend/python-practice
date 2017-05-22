class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters=set()
        front=end=0
        ret=float('-inf')

        while front<len(s):
            if s[front] in letters:
                ret=max(ret,front-end)
                while s[end]!=s[front] and end<=front:

                    import ipdb; ipdb.set_trace()

                    letters.remove(s[end])
                    end+=1
                end+=1
            letters.add(s[front])
            front+=1

        ret=max(ret,front-end)
        return ret

print Solution().lengthOfLongestSubstring('abcabcbb')
# ok, but not best solution, only so so, too many bad steps so as to redudent.
