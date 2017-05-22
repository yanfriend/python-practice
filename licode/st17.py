class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        self.map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }


        self.ret=[]
        if not digits: return self.ret

        self.dfs(digits,0,'')
        return self.ret

    def dfs(self,digits,ind, partial_word):
        if ind>=len(digits):
            self.ret.append(partial_word)
            return

        letters=self.map[digits[ind]]
        for l in letters:
            self.dfs(digits, ind+1, partial_word+l)

