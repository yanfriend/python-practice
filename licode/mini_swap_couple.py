class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        root = [i for i in range(n / 2)]
        cnt = n / 2

        def find(node):
            if root[node] == node: return node
            root[node]=find(root[node])
            return root[node]

        for i in range(0, n, 2):
            if find(row[i] / 2) != find(row[i + 1] / 2):
                root[find(row[i] / 2)] = find(row[i + 1] / 2)
                cnt -= 1
        return n / 2 - cnt
#
print Solution().minSwapsCouples([5,4,2,6,3,1,0,7]) # 2
