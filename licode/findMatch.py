def findMatch(n):
    grp=[str(i+1) for i in range(n)]
    return findContestMatch(n,grp)[0]


def findContestMatch(n,grp):
    """
    :rtype:str
    """
    if not n: return ''
    if n==1: return grp

    for ind in range(len(grp)/2):
        grp[ind]=str('('+grp[ind]+ ','+grp[len(grp)-ind-1] +')')
    return findContestMatch(n/2,grp[:len(grp)/2])

print findMatch(8)
