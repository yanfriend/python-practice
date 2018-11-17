class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import collections
        count = collections.Counter(S)

        ds = []
        for k, cnt in count.most_common():
            if count[k] > (len(S) + 1) / 2: return ''
            ds.extend(k * count[k])
        ans = [None] * len(S)
        ans[::2], ans[1::2] = ds[:(len(S) + 1) / 2], ds[(len(S) + 1) / 2:]
        return ''.join(ans)


print Solution().reorganizeString('aba')
