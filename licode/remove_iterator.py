class Iterator(object):

    def __init__(self, values):
        self.values = values
        self.row = self.col = 0

    def hasnext(self):
        while self.row < len(self.values) and \
                self.col == len(self.values[self.row]): # mistake two, use while, and order with next block
            self.row += 1
            self.col = 0

        if self.row == len(self.values) and self.col == len(self.values[self.row]):
            return False

        return True

    def getnext(self):
        # has called has_next
        self.col += 1
        return self.values[self.row][self.col - 1]

    def remove(self):
        # called after next()
        del self.values[self.row][self.col - 1]
        self.col -= 1  # mistake one, not deduct


iter = Iterator([[1, 2], [], [3]])
print iter.hasnext()
print iter.getnext()
print iter.hasnext()
print iter.getnext()
print iter.remove()

print iter.values

print iter.hasnext()
print iter.getnext()
print iter.remove()

print iter.values

# [ [1,2], [3], [4,5,6] ]
