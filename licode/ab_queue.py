class ABNode(object):
    def __init__(self):
        self.array=[0]*5
        self.next=None

class ABQueue(object):
    def __init__(self):
        self.frontq=self.endq=ABNode()
        self.size=0
        self.frontp=self.endp=0

    def push(self, num):
        if self.endp>=5:
            next_node=ABNode()
            self.endq.next=next_node
            self.endq=self.endq.next
            self.endp=0
        self.endq.array[self.endp]=num
        self.endp+=1
        self.size+=1

    def pop(self):
        if self.size==0:
            raise Exception('empty queue')
        self.size-=1
        tmp=self.frontq.array[self.frontp]
        self.frontp+=1
        if self.frontp==5:
            self.frontq=self.frontq.next
            self.frontp=0
        return tmp

abq=ABQueue()
abq.push(1)
abq.push(2)
abq.push(3)
abq.push(4)
abq.push(5)
abq.push(6)
abq.push(7)
abq.push(8)
abq.push(9)
abq.push(10)
abq.push(11)

while abq.size>0:
    print abq.pop()

abq.pop()

