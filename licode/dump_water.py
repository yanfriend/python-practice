# water with walls

def print_water(heights, water):
    highest = max([water[i] + heights[i] for i in range(len(heights))])
    for h in range(highest, -1, -1):
        for i in range(len(heights)):
            if heights[i] + water[i] < h:
                print ' ',
            elif heights[i] < h:
                print 'w',
            else:
                print '*',
        print ''


def dump_water(land, pos, amount):
    water=[0]*len(land)
    while amount>0:
        l=r=put_position=pos
        while l>0:
            if water[l]+land[l]<water[l-1]+land[l-1]: # find up on left
                put_position=l
                break
            l-=1
        if water[put_position]+land[put_position]>=water[pos]+land[pos]: # left same level, try right
            while r<len(water)-1:
                if water[r]+land[r]<water[r+1]+land[r+1]:
                    put_position=r
                    break
                r+=1

        left_max=max(land[:put_position])
        right_max=max(land[put_position+1:])

        if water[put_position]+land[put_position] >= min(left_max, right_max):
            return water

        water[put_position]+=1
        print_water(land, water)
        amount-=1

    return water

# print dump_water([3,2,1,2], 1, 2)  # [0,0,1,0] put extra in dumpposition

# waterLand = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4] # all correct
# print dump_water(waterLand, 5, 1);
# print dump_water(waterLand, 5, 5);
# print dump_water(waterLand, 5, 10);
# print dump_water(waterLand, 5, 20);
# print dump_water(waterLand, 5, 30);
# print dump_water(waterLand, 5, 50);
# print dump_water(waterLand, 5, 100);

# waterLand = [3, 1, 1, 1, 2] # all correct
# print dump_water(waterLand, 2, 1);
# print dump_water(waterLand, 2, 5);

# waterLand = [3, 3, 3, 1, 2] # only add one at pos 4
# print dump_water(waterLand, 2, 1);
# print dump_water(waterLand, 2, 2);


# waterLand = [1, 1, 1, 1, 0, 2] # only add one at pos 4
# print dump_water(waterLand, 2, 1);
# print dump_water(waterLand, 2, 6);


# waterLand = [1, 1, 1, 1, 1] # all empty
# print dump_water(waterLand, 2, 1);

waterLand = [2,1,0,3,2,6]
print dump_water(waterLand, 4, 100);
