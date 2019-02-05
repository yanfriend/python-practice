class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = [0] * n
        visited = set()
        visited.add(tuple(ans)) # error 2, add and set directly are diff
        total = k ** n

        def helper():
            if len(visited) == total:
                return
            prefix = ans[-n:]
            for i in range(k-1,-1,-1): # error 3, order!
                curr = prefix + [i]
                curr = tuple(curr[-n:]) # error 1, used -n+1
                if curr in visited: continue
                visited.add(curr)
                ans.append(i)
                helper()

        helper()
        return ''.join(map(str, ans))

print Solution().crackSafe(1,2)

print Solution().crackSafe(2,3)
