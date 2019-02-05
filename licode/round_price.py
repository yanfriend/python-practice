
def round_price(prices):

    sumup=round(sum(prices))

    truncated = [int(p) for p in prices]
    truncsum=sum(truncated)

    remaining=[(prices[i]-truncated[i], i) for i in range(len(prices))]
    remaining.sort(reverse=True)

    for i in range(int(sumup)-truncsum):
        truncated[remaining[i][1]]+=1
    return truncated



print round_price( [1.2, 2.3, 3.4])

print round_price([30.3, 2.4, 3.5])  # 30,2,4; +1 from the biggest diff
print round_price([30.9, 2.4, 3.9]) # 31 2 4; sum and round
