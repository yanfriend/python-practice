


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0

        points=sorted(points,key=lambda x:x[1])

        import ipdb; ipdb.set_trace()

        ret=1
        cut=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=cut:
                pass
                # cut=points[i][1]
            else:
                cut=points[i][1]
                ret+=1
        return ret

print Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])

