
def comb(primes):
    ret=[]
    helper(primes,0,1,ret)
    ret=ret[1:]
    return ret


def helper(primes,ind, prod,ret):
    ret.append(prod)
    for i in range(ind,len(primes)):
        helper(primes,i+1,prod*primes[i],ret) # a mistake, *primes[i], not primes[ind]


print comb([2,3,5])
