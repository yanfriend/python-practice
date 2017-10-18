import copy


def road_len(road): # [0 1 1 1 1 0 0 0 1 1 0]

    ret=copy.deepcopy(road)

    for i in range(len(road)):
        if road[i]==0: continue
        ret[i]+=0 if i==0 else ret[i-1]

    override_val=0
    for i in range(len(ret)-1,-1,-1):
        if ret[i]!=0:
            if override_val==0: override_val=ret[i]
            else: ret[i]=override_val
        else:
            override_val=0

    return ret

print road_len([0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0])  # 0, 4,4,4,4, 0,0,0, 2,2, 0

# two dp one from left, one from right are fine.
