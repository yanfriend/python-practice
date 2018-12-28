
def palindromePairs(words):

    mp={w:i for i,w in enumerate(words)}
    res=[]

    def is_palin(word):
        return word==word[::-1]

    for i,w in enumerate(words):
        n=len(w)+1
        for j in range(n):
            left=w[:j][::-1] # reverted
            right=w[j:][::-1]
            if left in mp and is_palin(right) and i!=mp[left] and j!=n-1: # not itself, not two '' match
                res.append([i, mp[left]])
            if right in mp and is_palin(left) and i!=mp[right]:
                res.append([mp[right],i])

    return res


print palindromePairs(["abcd","dcba","tob","ot", ""])

print palindromePairs(['aba', ''])  # [0,1] [1,0]
