import collections


def minWindow(s, t):
    counter=collections.Counter(t)
    cnt=len(t)
    ret=float('inf')
    ret_ind=0
    begin_ind=0

    for i,ch in enumerate(s):
        counter[ch]-=1
        if counter[ch]>=0: # here
            cnt-=1

        while cnt==0:
            if i-begin_ind+1<ret:
                ret=i-begin_ind+1
                ret_ind=begin_ind
            ret=min(ret,i-begin_ind+1)
            # advance being_ind
            counter[s[begin_ind]]+=1
            if counter[s[begin_ind]]==1:
                cnt+=1
            begin_ind+=1

    return s[ret_ind:ret_ind+ret] if ret!=float('inf') else ''

print minWindow('abcdef','acde')
