import collections


def ski_trails_bfs(trails, points, targets):
    rewards={k:float('-inf') for k in points}
    parents={}
    graph=collections.defaultdict(dict)

    for trail in trails:
        s,t,dist=trail.split(',')
        graph[s][t]=int(dist)

    qu=['a']
    rewards['a']=points['a']
    while len(qu)>0:
        new=[]
        for p in qu:
            for nei in graph[p]:
                if rewards[nei]<rewards[p]+graph[p][nei]+points[nei]:
                    rewards[nei]=rewards[p]+graph[p][nei]+points[nei]
                    new.append(nei)
                    parents[nei]=p
        qu=new

    max_t=None; max_val=0
    for d in targets:
        if rewards[d]>max_val:
            max_val=rewards[d]
            max_t=d
    path=[]
    while max_t in parents:
        path.append(max_t)
        max_t=parents[max_t]
    path=['a']+path[::-1]

    return max_val, path


def ski_trails_topo(trails, points, targets):
    rewards={k:float('-inf') for k in points}
    rewards['a']=points['a']

    parents={}
    graph=collections.defaultdict(dict)

    for trail in trails:
        s,t,dist=trail.split(',')
        graph[s][t]=int(dist)

    topo_path=[]
    def topo(node):
        for nei in graph[node]:
            topo(nei)
        topo_path.append(node)

    topo('a')
    # topo_path from back to front
    for node in reversed(topo_path):
        for nei in graph[node]:
            if rewards[nei] < rewards[node] + graph[node][nei] + points[nei]:
                rewards[nei] = rewards[node] + graph[node][nei] + points[nei]
                parents[nei] = node

    # find parents below
    max_t=None; max_val=0
    for d in targets:
        if rewards[d]>max_val:
            max_val=rewards[d]
            max_t=d
    path=[]
    while max_t in parents:
        path.append(max_t)
        max_t=parents[max_t]
    path=['a']+path[::-1]

    return max_val, path


trails=[
    'a,b,2',
    'a,c,3',
    'b,d,5',
    'b,e,6',
    'c,e,4',
    'c,f,4',
    'd,h,7',
    'e,h,6',
    'h,i,1',
    'h,j,2',
    'f,j,3'
]
points={
    'a': 5,
    'b': 7,
    'c': 6,
    'd': 2,
    'e': 1,
    'f': 7,
    'h': 7,
    'i': 3,
    'j': 2,
}

# print ski_trails_bfs(trails, points, ['i', 'j']) # (39, ['a', 'b', 'd', 'h', 'i'])

print ski_trails_topo(trails, points, ['i', 'j']) # (39, ['a', 'b', 'd', 'h', 'i'])

