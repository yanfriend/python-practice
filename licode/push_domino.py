class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        ans = []
        for i, val in enumerate(dominoes):  # R down first
            if val == 'R':
                ans.append(('R', 0))
            elif val == 'L':
                ans.append(('L', 0))
            else:
                if ans and ans[-1][0] == 'R':
                    ans.append(('R', ans[-1][1] + 1))
                else:
                    ans.append(('.', 0))
        for i in range(len(dominoes) - 1, -1, -1):
            letter = dominoes[i]
            if letter == 'L': continue
            if i + 1 < len(dominoes) and ans[i + 1][0] == 'L':
                if ans[i][0] == '.':
                    ans[i] = ('L', ans[i + 1][1] + 1)
                elif ans[i][0] == 'R':
                    if ans[i + 1][1] + 1 < ans[i][1]:
                        ans[i] = ('L', ans[i + 1][1] + 1)
                    elif ans[i + 1][1] + 1 == ans[i][1]:
                        ans[i] = ('.', 0)

        return ''.join(x for x, i in ans)

print Solution().pushDominoes(".L.R...LR..L..")
