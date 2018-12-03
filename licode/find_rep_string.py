class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # sorted_index = reversed(sorted((val,i) for i, val in enumerate(indexes)))
        sorted_index=sorted(zip(indexes, sources, targets), reverse=True)
        ans = S
        for ind, s, t in sorted_index:
            # s=sources[original_index]; t=targets[original_index]
            if ans[ind:].startswith(s): ans = ans[:ind] + ans[ind:].replace(s, t, 1)
        return ans

print Solution().findReplaceString(
    "vmokgggqzp",
    [3, 5, 1],
    ["kg", "ggq", "mo"],
    ["s", "so", "bfr"]
)
