import collections

Map=lambda : collections.defaultdict(Map)
value=1


class Solution(object):
    def __init__(self):
        self.mp=Map()

    def create(self, path, val):
        folders = path.split('/')[1:] # skip init '' from /
        tmp=self.mp
        for f in folders[:-1]:
            if f in tmp:
                tmp=tmp[f]
            else:
                return False
        tmp=tmp[folders[-1]]
        tmp[value]=val

    def get(self, path):
        folders = path.split('/')[1:]
        tmp = self.mp
        for f in folders:
            if f in tmp:
                tmp=tmp[f]
            else:
                return False
        return tmp[value]

sol=Solution()

print sol.create('/a',1) # ok.
print sol.get('/a')

print sol.create('/a/b',2)
print sol.get('/a/b')

print sol.create('/a/b/c',3) # ok.
print sol.get('/a/b')

print sol.create('/c/d', 2) # err
print sol.get('/c') # err


