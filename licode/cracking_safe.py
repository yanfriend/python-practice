class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = set()
        ans = []

        def dfs(node):
            for ch in map(str, range(k)):
                if node + ch not in visited:
                    visited.add(node + ch)
                    dfs((node + ch)[1:])
                    ans.append(ch)

        dfs('0' * (n - 1))
        return ''.join(ans) + '0' * (n - 1)  # add original state


print Solution().crackSafe(2,2) # 01100

print Solution().crackSafe(2,3) # 0221120100   : 02,22,21,11,12,20,01,10,00
