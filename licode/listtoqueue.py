FIX_SIZE=4

class ListNode(object):
    def __init__(self):
        self.next=None
        self.vals=[] # if this fixed, use two indexes for front and end. Don't have to from Deep autumn version

class Solution(object):

    def __init__(self):
        self.count=0
        self.head=self.tail=ListNode()
        self.head_ind=0

    def put(self, val):
        if len(self.tail.vals)>=FIX_SIZE:
            tmp=ListNode()
            self.tail.next=tmp
            self.tail=self.tail.next
        self.tail.vals.append(val)
        self.count+=1

    def get(self):
        if self.head_ind>=len(self.head.vals) and self.head.next is None:
            raise Exception('no addtional values')
        if self.head_ind>=len(self.head.vals):
            self.head=self.head.next
            self.head_ind=0
        self.count-=1
        val=self.head.vals[self.head_ind]
        self.head_ind+=1
        return val

    def size(self):
        return self.count


queue=Solution()
queue.put(8)
queue.put(7)
queue.put(6)
queue.put(5)
queue.put(4)
queue.put(3)
queue.put(2)
queue.put(1)
queue.put(0)

while queue.size()>0:
    print queue.get()

# print queue.get() # exceptions, correct

queue.put(10)
print queue.get()
