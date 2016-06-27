class p():
    def __init__(self, x, y):
        self.x=x ; self.y=y
    def __repr__(self):
        return "(%r,%r)"%(self.x,self.y)
    def __add__(self, P):
        return p(self.x+P.x, self.y+P.y)

pts=[p(1,0), p(2,1), p(-3,4)]
from operator import add
print reduce(add,pts)

print sum(pts[1:], pts[0])
