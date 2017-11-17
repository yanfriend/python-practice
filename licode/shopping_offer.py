class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        import ipdb; ipdb.set_trace()

        ret=float('inf')
        for sp in special:
            can_use=True
            for i in range(len(needs)):
                if sp[i]>needs[i]: # too big in special
                    can_use=False
                    break

            if can_use: # deduct, recursion, and add back
                for i in range(len(needs)):
                    needs[i]-=sp[i]
                ret=min(ret,self.shoppingOffers(price,special,needs)+sp[len(needs)])
                for i in range(len(needs)):
                    needs[i]+=sp[i]

        # can't use special for (remaining)needs
        sm=0
        for i in range(len(needs)):
            sm+=needs[i]*price[i]
        return min(ret,sm)

print Solution().shoppingOffers(
    [2,5],
    [[3,0,5],[1,2,10]],
    [3,2]
)

