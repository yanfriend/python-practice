

def collatz(n):
    ret=1
    while n>1:
        if n%2: # odd
            n=3*n+1
        else:
            n/=2
        ret+=1
    return ret

print collatz(7)

