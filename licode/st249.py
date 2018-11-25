import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        :type string: list of strings
        :rtype: list of list of strings
        """
        grps=collections.defaultdict(list)
        for w in strings:
            grps[self.my_hash(w)].append(w)

        ret=[]
        for v in grps.values():
            ret.append(sorted(v))
        return ret

    def my_hash(self,word):
        diff=ord(word[0])-ord('a')
        ret=[]
        for lt in word:
            ret.append(chr(((ord(lt)-diff)%26)+ord('a')))
        return ''.join(ret)

print Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
