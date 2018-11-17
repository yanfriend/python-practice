class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx > sx and ty > sy:
            if ty > tx:
                ty %= tx
            else:
                tx %= ty
        return (ty == sy or bool(tx) and (ty - sy) % sx == 0) and (sx == tx or bool(ty) and (tx - sx) % sy == 0)


print Solution().reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5) # T
print Solution().reachingPoints(sx=10, sy=1, tx=17, ty=17) # F
