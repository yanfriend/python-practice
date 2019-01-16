
class Solution(object):
    def print_water(self, heights, water):
        highest = max([water[i]+heights[i] for i in range(len(heights))])
        for h in range(highest, -1, -1):
            for i in range(len(heights)):
                if heights[i]+water[i]<h: print ' ',
                elif heights[i]<h: print 'w',
                else: print '*',
            print ''

    def fill_water(self, heights, position, count):
        n=len(heights)
        water=[0]*n

        while count>0:
            put_pos=l=r=position
            while l>0:
                if heights[l-1]+water[l-1] > heights[l]+water[l]: break # find wall to left
                l-=1
            if heights[l]+water[l] < heights[position]+water[position]: # and it's a down pit
                put_pos=l
            else:
                while r<n-1:
                    if heights[r+1]+water[r+1]>heights[r]+water[r]: break # find wall to right, to break
                    r+=1
                if heights[r]+water[r] < heights[position]+water[position]: # and it's a down pit
                    put_pos=r

            if put_pos==0 or put_pos==n-1: break  # at border, cant fill. the below four lines added by me.
            maxh_left=max(heights[0:put_pos])
            maxh_right=max(heights[put_pos+1:])
            if water[put_pos]+1+heights[put_pos] > min(maxh_left, maxh_right): break  # out of border

            water[put_pos]+=1
            count-=1

        self.print_water(heights, water)
        return water


    def pourWater_huahua(self, heights, V, K):
        """
        drops to K first if all flat
        :param heights:
        :param V:
        :param K:
        :return:
        """
        def drop(h, K):
            best = K
            for d in (-1, 1):
                i = K + d
                while i >= 0 and i < len(h) and h[i] <= h[i - d]:
                    if h[i] < h[best]:
                        best = i
                    i += d
                if best != K:
                    break
            heights[best] += 1

        for _ in range(V):
            drop(heights, K)
        return heights

# print Solution().fill_water([3,2,1,2], 1, 2)  # [0,1,1,0] put extra in dumpposition

# waterLand = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4] # all correct
# print Solution().fill_water(waterLand, 5, 1);
# print Solution().fill_water(waterLand, 5, 5);
# print Solution().fill_water(waterLand, 5, 10);
# print Solution().fill_water(waterLand, 5, 20);
# print Solution().fill_water(waterLand, 5, 30);
# print Solution().fill_water(waterLand, 5, 50);
# print Solution().fill_water(waterLand, 5, 100);

waterLand = [3, 1, 1, 1, 2] # all correct
# print Solution().pourWater_huahua(waterLand, 1, 2); # huahua's
# print Solution().pourWater_huahua(waterLand, 4, 2);
# print Solution().fill_water(waterLand, 2, 1);
# print Solution().fill_water(waterLand, 2, 5);


# waterLand = [3, 3, 3, 1, 2] # only add one at pos 4
# print Solution().fill_water(waterLand, 2, 1);
# print Solution().fill_water(waterLand, 2, 2);


# waterLand = [1, 1, 1, 1, 0, 2] # only add one at pos 4
# print Solution().fill_water(waterLand, 2, 1);
# print Solution().fill_water(waterLand, 2, 6);


waterLand = [1, 1, 1, 1, 1] # all empty
print Solution().fill_water(waterLand, 2, 1);

