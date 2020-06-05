def numKLenSubstrNoRepeats(S,K):
    uniques = set()
    l=0
    ret=0
    for r in range(len(S)):
        while S[r] in uniques:
            uniques.remove(S[l]); l+=1
        uniques.add(S[r])
        if len(uniques)>=K:
            uniques.remove(S[l]); l+=1
            ret+=1
    return ret

print numKLenSubstrNoRepeats(S = "havefunonleetcode", K = 5)
print numKLenSubstrNoRepeats(S = "home", K = 5)
