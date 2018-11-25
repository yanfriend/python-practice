
def maxprod(matrix):
    cache={}
    ret=[0]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            visited=set([(i,j)])
            helper(matrix, cache, ret, matrix[i][j], ((i,j),), visited)
    return ret[0]

def helper(matrix, cache, ret, prod, path, visited):
    if len(path)==4:
        ret[0]=max(ret[0],prod)
        return

    #if tuple(sorted(path)) in cache:
    #    return cache[tuple(sorted(path))]

    dir=((0,1),(0,-1),(1,0),(-1,0))
    for di,dj in dir:
        ni=path[-1][0]+di
        nj=path[-1][1]+dj
        if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and (ni,nj) not in visited:
            # import ipdb; ipdb.set_trace()

            visited.add((ni,nj),)
            helper(matrix, cache, ret, prod*matrix[ni][nj], path+((ni,nj),), visited)
            visited.discard((ni,nj),)


matrix=[
    [1,2,1,1,],
    [0,4,3,0],
    [0,2,0,0],
    [1,1,1,1]
]
print maxprod(matrix)
