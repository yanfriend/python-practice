import collections


def min_win_subs(s,t):
    # s is original str, t is pattern
    counter = collections.Counter(t)
    needed = len(t)
    ret_len=float('inf')
    ret_ind=0; begin_ind=0

    for i in range(len(s)):
        counter[s[i]] -= 1
        if counter[s[i]] >= 0:
            needed -= 1

        while needed == 0:
            if i-begin_ind+1<ret_len:
                ret_len=i-begin_ind+1
                ret_ind=begin_ind
            counter[s[begin_ind]] += 1
            if counter[s[begin_ind]] > 0:
                needed += 1
            begin_ind+=1

    return s[ret_ind:ret_len+ret_ind] if ret_len!=float('inf') else ''

    # two mistakes: 1, miss begin_ind. 2, miss ret_ind+ret_len
