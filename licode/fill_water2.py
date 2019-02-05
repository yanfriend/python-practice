class Solution(object):

    # print water. copied from previous version
    def print_water(self, heights, water):
        highest = max([water[i]+heights[i] for i in range(len(heights))])
        for h in range(highest, -1, -1):
            for i in range(len(heights)):
                if heights[i]+water[i]<h: print ' ',
                elif heights[i]<h: print 'w',
                else: print '*',
            print ''

    def fill_water(self, land, drop_pos, amount):
        water=[0]*len(land)

        while amount>0:
            l=r=put_pos=drop_pos
            while l>0:
                if land[l]+water[l]<land[l-1]+water[l-1]:  # find left up
                    put_pos=l; break
                l-=1

            if put_pos==drop_pos or land[put_pos]+water[put_pos]>=land[drop_pos]+water[drop_pos]:
                # error 1, missed after or. it caused add to left even it's higher than drop pos, and right side
                while r<len(land)-1:
                    if land[r]+water[r]<land[r+1]+water[r+1]:
                        put_pos=r
                        break
                    r+=1

            left_max=max(land[:put_pos])
            right_max=max(land[put_pos+1:])
            if water[put_pos] + land[put_pos] >= min(left_max, right_max):
                break
            water[put_pos] += 1
            amount-=1
            self.print_water(land, water)


# waterLand = [2,1,0,3,2,6]
# print Solution().fill_water(waterLand, 4, 100);

# waterLand = [3, 3, 3, 1, 2] # only add one at pos 4
# print Solution().fill_water(waterLand, 2, 1);
# print Solution().fill_water(waterLand, 2, 2);


# waterLand = [1, 1, 1, 1, 0, 2] # only add one at pos 4
# print Solution().fill_water(waterLand, 2, 1);
# print Solution().fill_water(waterLand, 2, 6);


# waterLand = [1, 1, 1, 1, 1] # all empty
# print Solution().fill_water(waterLand, 2, 1);

waterLand = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4] # all correct
print Solution().fill_water(waterLand, 5, 1);
print Solution().fill_water(waterLand, 5, 5);
print Solution().fill_water(waterLand, 5, 10);
print Solution().fill_water(waterLand, 5, 20);
print Solution().fill_water(waterLand, 5, 30);
print Solution().fill_water(waterLand, 5, 50);
print Solution().fill_water(waterLand, 5, 100);
'''
caused below error
*                       
* * w                 * 
* * w w w *           * 
* * * w * * *       * * 
* * * * * * * *   * * * 
* * * * * * * * * * * * 


* *         w w w w w * 
* * w w w * w w w w w * 
* * * w * * * w w w * * 
* * * * * * * * w * * * 
* * * * * * * * * * * * 
*                       
* *       w w w w w w * 
* * w w w * w w w w w * 
* * * w * * * w w w * * 
* * * * * * * * w * * * 
* * * * * * * * * * * *   # so far, it fills to right side. cos put_pos amount == drop_pos, try right
*                       
* * w     w w w w w w *   # after fills drop_pos, it fills to left side. cos put_pos amount < drop_pos
* * w w w * w w w w w * 
* * * w * * * w w w * * 
* * * * * * * * w * * * 
* * * * * * * * * * * * 
*                       
* * w w   w w w w w w * 
* * w w w * w w w w w * 
* * * w * * * w w w * * 
* * * * * * * * w * * * 
* * * * * * * * * * * * 
*                       
'''
