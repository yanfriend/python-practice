class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        import collections
        group = collections.Counter(map(lambda x: sum(map(int, str(x))), range(1, n + 1))).most_common()
        print group

        return sum(v == group[0][1] for k, v in group)

print Solution().countLargestGroup(13)

