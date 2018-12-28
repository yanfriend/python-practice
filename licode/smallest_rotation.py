class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        changes = [0] * N  # changes[i] means in i turns, score changes
        for i in range(N): changes[(i - A[i] + N + 1) % N] -= 1
        for i in range(1, N): changes[i] += changes[i - 1] + 1  # +1, one moved to N-1, so index is always larger
        return changes.index(max(changes))


print Solution().bestRotation([2, 3, 1, 4, 0])
