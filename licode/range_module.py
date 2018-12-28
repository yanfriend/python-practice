import bisect


class RangeModule(object):

    def __init__(self):
        self.range = [float('-inf'), float('inf')]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.update(left, right, 0)

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        li = bisect.bisect_right(self.range, left)
        ri = bisect.bisect_left(self.range, right)
        return (li == ri) and (li % 2 == 0)

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.update(left, right, 1)

    def update(self, left, right, val):
        li = bisect.bisect_left(self.range, left)
        ri = bisect.bisect_right(self.range, right)

        if li % 2 == val:
            li -= 1
            left = self.range[li]
        if ri % 2 == val:
            right = self.range[ri]
            ri += 1
        self.range[li:ri] = [left, right]

# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10,20)
obj.removeRange(14, 16)
obj.removeRange(12,15)

print obj.queryRange(10,14)

