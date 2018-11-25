import copy

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict=set(wordDict)
        memo={len(s):['']}
        return self.breaker(s,wordDict,0,memo)

    def breaker(self,s,wordDict,ind,memo):
        if ind in memo:
            return memo[ind]

        ret=[]
        for i in range(ind+1,len(s)+1):
            if s[ind:i] in wordDict:

                import ipdb; ipdb.set_trace()

                tails=self.breaker(s,wordDict,i,memo)
                for t in tails:
                    ret.append(s[ind:i]+' '+t) # changed in submission
        memo[ind]=ret # copy.deepcopy(ret)
        return memo[ind]

print Solution().wordBreak('abcdef',['abc','def'])
