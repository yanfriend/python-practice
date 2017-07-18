import collections

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        my_dict=collections.defaultdict(list)
        ele_hash=0
        ele=''
        ch_int={'A':2,'C':3,'G':5,'T':7}

        for ch in s:
            ele+=ch
            ele_hash=ele_hash*10+ch_int[ch]
            if len(ele)<10:
                continue
            elif len(ele)>10:
                ele_hash-=ch_int[ele[0]]*(10**10)
                ele=ele[1:]
            my_dict[ele_hash].append(ele)

        ret=[]
        for k,v in my_dict.items():
            if len(v)>1:
                ret.append(v[0]) # extend(v)
        return ret

print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
# v1 passed
