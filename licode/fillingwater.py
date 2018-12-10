

class Solution(object):
    def fill_water(self, heights, position, count):
        n=len(heights)
        water=[0]*n

        while count>0:
            put_pos=l=r=position
            while l>=1:
                if heights[l-1]+water[l-1] > heights[l]+water[l]: break
                l-=1
            if heights[l]+water[l] < heights[position]+water[position]:
                put_pos=l
            else:
                while r<n-1:
                    if heights[r+1]+water[r+1]>heights[r]+water[r]: break
                    r+=1
                if heights[r]+water[r] < heights[position]+water[position]:
                    put_pos=r

            maxh_left=max(heights[0:put_pos]) # the below three lines added by me.
            maxh_right=max(heights[put_pos+1:])
            if water[put_pos]+1+heights[put_pos] > min(maxh_left, maxh_right): break  # out of border

            water[put_pos]+=1
            count-=1

        highest = max([water[i]+heights[i] for i in range(len(heights))])
        for h in range(highest, -1, -1):
            for i in range(len(heights)):
                if heights[i]+water[i]<h: print ' ',
                elif heights[i]<h: print 'w',
                else: print '*',
            print ''

        return water



# print Solution().fill_water([3,2,1,2], 1, 2)  # [0,1,1,0] put extra in dumpposition

waterLand = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]
print Solution().fill_water(waterLand, 5, 1);
print Solution().fill_water(waterLand, 5, 5);
print Solution().fill_water(waterLand, 5, 10);
print Solution().fill_water(waterLand, 5, 20);
print Solution().fill_water(waterLand, 5, 30);
print Solution().fill_water(waterLand, 5, 50); # water up?
print Solution().fill_water(waterLand, 5, 100);
