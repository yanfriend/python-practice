class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mp={}
        ret=[]
        for i in range(len(words)): mp[words[i]]=i
        for i in range(len(words)):
            nw=words[i][::-1]

            import ipdb; ipdb.set_trace()

            for j in range(len(nw)):
                left=nw[:j]; right=nw[j:]
                if self.is_palin(right) and left in mp and mp[left]!=i:
                    ret.append([mp[left],i])
                    if left=='':
                        ret.append(i,mp[left])
                if self.is_palin(left) and right in mp and mp[right]!=i:
                    ret.append([i,mp[right]])


        return ret

    def is_palin(self,word):
        l=0;r=len(word)-1
        while l<r:
            if word[l]==word[r]:
                l+=1; r-=1
            else: return False
        return True

# print Solution().palindromePairs(['a',''])
print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])

