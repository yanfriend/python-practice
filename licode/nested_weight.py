def depthSumInverse(nestedList):
    ret=[0]
    helper(nestedList, ret)
    return ret[0]

def helper(nestedList, ret):
    maxh=0
    my_sum=0
    for nl in nestedList:
        if type(nl)==int:
            my_sum+=nl
        else:
            maxh=max(maxh,helper(nl,ret))
    maxh+=1
    ret[0]+=my_sum*maxh
    return maxh

print depthSumInverse([[1,1],2,[1,1]]) # expect weight, 8
print depthSumInverse([1,[4,[6]]]) # expect weight, 17
