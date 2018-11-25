
def max_profit(prices,commission): # sell commission
    ret=0;
    entry=float('inf')
    this_max=0

    for price in prices:
        # import ipdb; ipdb.set_trace()

        this_max=max(this_max,price-entry-commission)

        if this_max>0 and this_max>price-entry:
            entry=price
            ret+=this_max
            this_max=0
        elif entry>price:
            entry=price

    return ret+this_max


print max_profit([1,5,2,3,8,4],2) # 2+4=6

print max_profit([1,5,4,8],2) # 2+2=4, or 8-1-2=5, the latter is better!

print max_profit([1,5,4],2) # 2

print max_profit([1,5,4,1,8],2) # 2+5=7
