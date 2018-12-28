import collections

def helper(account, start, cnt):
    ans=float('inf')
    while start<len(account) and account[start]==0: start+=1
    for i in range(start+1, len(account)):
        if account[i]*account[start]<0:
            account[i]+=account[start]  # transfer account start to account i
            ans=min(ans,helper(account, start+1, cnt+1)) # issue 1, start, not i
            account[i]-=account[start]
    return cnt if ans==float('inf') else ans # issue 2, if not in loop

def minTransfers(transactions):
    transfers=collections.defaultdict(int)
    for t in transactions:
        transfers[t[0]]-=t[2]
        transfers[t[1]]+=t[2]

    accounts=[]
    for val in transfers.values():
        if val!=0: accounts.append(val)

    return helper(accounts, 0, 0)


print minTransfers([[0,1,10], [2,0,5]])   # 2

print minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])  # 1
