import collections


def shortestDistance(grid):
    # start from content 1, calculate distance to all 0's
    m=len(grid)
    n=len(grid[0])
    distances=[[0]*n for _ in range(m)] # 0 node in grid, distances to all 1's
    cnt=[[0]*n for _ in range(m)] # 0 node in grid, all 1 nodes it can reach.

    buildings=sum(val for line in grid for val in line if val==1)

    def bfs(x,y): # x,y is 1 in grid
        visited=set()
        qu=collections.deque()
        qu.append((x,y,0))
        visited.add((x,y))
        this_cnt=1  # count itself as buildings reached.

        while qu:
            i,j,dist=qu.popleft()
            delta=((0,1),(0,-1),(1,0),(-1,0))
            dist+=1
            for di,dj in delta:
                ni=i+di; nj=j+dj
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    if grid[ni][nj]==0:
                        qu.append((ni,nj,dist))
                        cnt[ni][nj]+=1 # every ni,nj (0 node) can reached one more by 1 node.
                        distances[ni][nj]+=dist
                    elif grid[ni][nj]==1:
                        this_cnt+=1 # x, y reach one more 1

        return this_cnt==buildings

    ret=float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                if not bfs(i,j): return -1

    for i in range(m):
        for j in range(n):
            if grid[i][j]!=0: continue
            if cnt[i][j]!=buildings: continue
            ret=min(ret,distances[i][j])
    return -1 if ret==float('inf') else ret


grid = [[1, 0, 2, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]] # 1 building; 2 wall.
print shortestDistance(grid)  # 7, at (1,2)
