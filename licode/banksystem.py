"""
deposit(id, amount, ts)
withdraw(id, amount, ts)
balance(id, start_ts, end_ts) in log(n)
"""

import bisect

def balance(id, st, end):
    account_balance={
        id: [(1,200), (2,100), (3,1000), (4,200), (5,0)]
    }
    balance=account_balance[id]
    start_ind = bisect.bisect_right(balance, (st,float('inf')))
    end_ind = bisect.bisect_right(balance, (end, float('-inf')))
    return balance[start_ind][1], balance[end_ind][1]


print balance(1, 2, 4)
#  (1000, 200)

'''
bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. 
bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.

They are equivalent when the the element to be inserted is NOT present in the list. 
Hence, they are not equivalent when the element to be inserted is IN the list.
'''
