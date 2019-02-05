'''
refer:
https://github.com/allaboutjst/airbnb/blob/master/src/main/java/list_of_list_iterator/ListofListIterator.java
https://rextester.com/SWJH94490
'''

class Iterator2d(object):
    def __init__(self, list2d):
        self.row = 0
        self.col = 0
        self.list2d = list2d

    def has_next(self):
        if not self.list2d: return False

        while self.row < len(self.list2d) and self.col == len(self.list2d[self.row]):
            self.row += 1
            self.col = 0
        if self.row == len(self.list2d): return False
        return True

    def next(self):
        if self.has_next():
            val = self.list2d[self.row][self.col]
            self.col += 1
            return val
        raise Exception('no next')

    def remove(self):
        while self.col == 0 and self.row > 0:
            if self.row < len(self.list2d) and len(self.list2d[self.row]) == 0:
                del self.list2d[self.row]

            self.row -= 1
            self.col = len(self.list2d[self.row])

        if self.col == 0: raise Exception('nothing to remove')
        self.col -= 1
        val = self.list2d[self.row][self.col]
        del self.list2d[self.row][self.col]
        return val

# sol = Iterator2d([[2,3],[4,5,6]])
#
# while sol.has_next():
#     print sol.next()
# # sol.next()  # exception


# sol = Iterator2d([[2,3],[4,5,6]])
# while sol.has_next():
#     print sol.next()
#
# print sol.remove()
# print sol.remove()
# print sol.remove()
# print sol.remove()
#
# print 'after remove'
#
# print sol.list2d


# sol = Iterator2d([[1,2],[3]])
# print sol.has_next()
# print sol.next()
# print sol.has_next()
#
# print sol.remove()  # remove 1, or remove 2?
#
# print sol.has_next()
# print sol.next()


# sol = Iterator2d([[1,2],[3],[4,5,6]]) # this test is ok.
# print sol.has_next()
# print sol.next()
# print sol.remove()
#
# print 'after remove:'
# while sol.has_next():
#     print sol.next()  # [2,3,4,5,6]


sol = Iterator2d([[1,2],[3]])
print sol.has_next()
print sol.next()
print sol.has_next()
print sol.next()

print sol.remove()
print sol.has_next()
print sol.next()  # true, 3.


'''
It's not obligatory to call hasNext() because maybe you don't need to 
-- you know the size of the collection in advance, for example, and know how many calls to next() you can make.
'''
