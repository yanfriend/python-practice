class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        A.sort()
        ans = 0
        for i in range(len(A) - 2):
            psum = target - A[i]
            k = i + 1
            j = len(A) - 1;
            while k < j:
                if A[k] + A[j] < psum:
                    k += 1; continue
                elif A[k] + A[j] > psum:
                    j -= 1; continue
                elif A[k] != A[j]:  # get the number
                    kstart = k
                    while k < j and A[k] == A[k + 1]: k += 1
                    jstart = j
                    while j > k and A[j] == A[j - 1]: j -= 1
                    ans += (jstart - j + 1) * (k - kstart + 1)
                else:  # get the number, Aj==Ak
                    ans += (j - k) * (j - k + 1) / 2
                    break
                k += 1;
                j -= 1
        return ans % (10 ** 9 + 7)

print Solution().threeSumMulti([1,1,2,2,2,2], 5)
