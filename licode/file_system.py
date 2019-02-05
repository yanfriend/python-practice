import collections

Trie = lambda: collections.defaultdict(Trie)
value = 1


class Solution(object):
    def __init__(self):
        self.folder = Trie()
        self.watches = Trie()

    def create(self, path, val):
        folders = path.split('/')[1:]  # skip init '' from /
        curr = self.folder
        for f in folders[:-1]:
            if f in curr:
                curr = curr[f]
            else:
                return False
        curr = curr[folders[-1]]
        curr[value] = val

        curr = self.watches
        for f in folders:
            if f in curr:
                curr = curr[f]
                if curr[value]:
                    curr[value]()
            else:
                return False

    def get(self, path):
        folders = path.split('/')[1:]
        tmp = self.folder
        for f in folders:
            if f in tmp:
                tmp = tmp[f]
            else:
                return False
        return tmp[value]

    def watch(self, path, func):
        folders = path.split('/')[1:]  # skip init '' from /
        curr = self.watches
        for f in folders[:-1]:
            if f in curr:
                curr = curr[f]
            else:
                return False
        curr = curr[folders[-1]]
        curr[value] = func


sol = Solution()


def pt1():
    print 'yes'
def pt2():
    print 'no'

print sol.watch('/a', pt1)
print sol.watch('/a/b', pt2)

print sol.create('/a', 1)  # ok.
print sol.get('/a')

print sol.create('/a/b', 2)
print sol.get('/a/b')

#
# print sol.create('/a/b/c',3) # ok.
# print sol.get('/a/b')


# print sol.create('/c/d', 2) # err
# print sol.get('/c') # err
