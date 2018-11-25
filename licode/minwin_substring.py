import collections


def minWindow(s,t):
    counter=collections.Counter(t)
    needed=len(t)
    l=0
    min_len=float('inf')
    begin_index=0
    for i in range(len(s)):

        import ipdb;ipdb.set_trace()

        counter[s[i]]-=1
        if counter[s[i]]==0:
            needed-=1

        while needed==0:
            if min_len>i-l+1:
                min_len=i-l+1
                begin_index=l
            counter[s[l]]+=1
            if counter[s[l]]==1:
                needed+=1
            l+=1
    return '' if min_len==float('inf') else s[begin_index:begin_index+min_len]

# print minWindow("ADOBECODEBANC","ABC")  # "BANC"
print minWindow("aa","aa")  # "BANC"
