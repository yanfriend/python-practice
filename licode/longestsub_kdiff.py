def lengthOfLongestSubstringKDistinct(s,k):
    ret=float('-inf')
    begin_ind=0
    m={}

    for i,ch in enumerate(s):
        m[ch]=i
        while len(m)>k:
            if m[s[begin_ind]]==i: del m[s[begin_ind]]
            begin_ind+=1
        ret=max(ret,i-begin_ind+1)

    return ret

print lengthOfLongestSubstringKDistinct('abacdf',2)
