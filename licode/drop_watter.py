def pourWater(heights, V, K):
    """
    :param heights:
    :param V: v water
    :param K: index to drop
    :return:
    """
    n=len(heights)
    water=[0]*n
    for i in range(V):
        ind=K
        while ind-1>=0 and heights[ind-1]+water[ind-1]<heights[ind]+water[ind]: # error
            ind-=1
        if ind<K:
            water[ind]+=1
        else:
            ind=K
            while ind+1<n and heights[ind+1]+water[ind+1]<heights[ind]+water[ind]:
                ind+=1
            water[ind]+=1
    return [heights[i]+water[i] for i in range(n)]



print pourWater([2,1,1,2,1,2,2], V = 4, K = 3) # return [2,2,2,3,2,2,2]
print pourWater([1,2,3,4], V = 2, K = 2) # [2,3,3,4]

print pourWater([3,1,3], V = 5, K = 1) # [4,4,4]