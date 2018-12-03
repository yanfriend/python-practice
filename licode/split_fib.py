class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []

        def fib(n1, n2, k, ans):
            if k == len(S): return True
            if S[k:].startswith(str(n1 + n2)):
                ans.append(n1 + n2)
                return fib(n2, n1 + n2, k + len(str(n1 + n2)), ans)
            return False

        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                if S[i] == '0' and (j - i > 1): continue
                num1 = int(S[i:j])
                ans = [num1]
                for k in range(j + 1, len(S)):
                    if S[j] == '0' and k - j > 1: continue
                    num2 = int(S[j:k])
                    ans.append(num2)
                    if fib(num1, num2, k, ans): return ans
                    ans.pop()
            ans = []

        return ans

print Solution().splitIntoFibonacci("0123")
