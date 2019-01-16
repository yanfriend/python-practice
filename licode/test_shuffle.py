import random


def shuffle(n):
    ret=[i for i in range(n)]
    for i in range(n):
        ind=random.randint(i,n-1)
        ret[i],ret[ind]=ret[ind], ret[i]
    return ret

print shuffle(8)

print shuffle(10)


