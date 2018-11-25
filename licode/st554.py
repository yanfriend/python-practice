import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counter=collections.Counter()

        for a_wall in wall:
            plength=0
            for i,piece in enumerate(a_wall):
                if i==len(a_wall)-1: break
                plength+=piece
                counter[plength]+=1

        if len(counter)==0: return len(wall)

        return len(wall)-counter.most_common(1)[0][1] # most_common returns a list of tuple(k:cnt)
