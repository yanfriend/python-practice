class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        slist=S.split(' ')
        res=[]
        for s in slist:
            if s[0] in 'aeiouAEIOU':
                s=s+'ma'
            else:
                s=s[1:]+s[0]+'ma'
            res.append(s)
        return ' '.join([s+'a'*(i+1) for i,s in enumerate(res)])

print Solution().toGoatLatin("I speak Goat Latin")
