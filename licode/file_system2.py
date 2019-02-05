import collections

Trie = lambda: collections.defaultdict(Trie)
VALUE = 1


class Solution(object):
    def __init__(self):
        self.trie = Trie()

    def create(self, path, value):
        folders = path.split('/')[1:]
        prevs = folders[:-1]
        curr = self.trie
        for p in prevs:
            if p not in curr: return False
            curr = curr[p]
        curr = curr[folders[-1]]
        curr[VALUE] = value
        return True

    def get(self, path):
        folders = path.split('/')[1:]
        curr = self.trie
        for p in folders:
            if p not in curr: return False
            curr = curr[p]
        return curr[VALUE]


sol = Solution()

print sol.create('/a', 1)  # ok.
print sol.get('/a')

print sol.create('/a/b', 2)
print sol.get('/a/b')

print sol.create('/a/b/c', 3)  # ok.
print sol.get('/a/b')
print sol.get('/a/b/c')

print sol.create('/c/d', 2)  # err
print sol.get('/c')  # err
