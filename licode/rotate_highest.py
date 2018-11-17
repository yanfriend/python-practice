class Solution(object):
    def bestRotation(self, A):
        N = len(A)
        change = [1] * N
        for i in range(N): change[(i - A[i] + 1) % N] -= 1
        for i in range(1, N): change[i] += change[i - 1]
        return change.index(max(change))

print Solution().bestRotation([2, 3, 1, 4, 0]) # 4,0,2,3,1:
