class DlNode(object):
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.count=0
        self.dict={}
        self.head=DlNode(0,0)
        self.tail=DlNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        node=self.dict[key]
        self.move_to_tail(node)
        return node.val

    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.count-=1

    def add_to_tail(self,node):
        node.prev=self.tail.prev
        node.next=self.tail
        self.tail.prev.next=node
        self.tail.prev=node
        self.count+=1

    def move_to_tail(self,node): # use remove and add to tail
        self.remove(node)
        self.add_to_tail(node)

    def remove_from_head(self):
        node=self.head.next
        if node==self.tail: return

        self.head.next=node.next
        node.next.prev=self.head
        del self.dict[node.key]
        self.count-=1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.dict:
            node=self.dict[key]
            node.val=value
            self.move_to_tail(node)
            return

        node=DlNode(key,value)
        if self.count>=self.capacity:
            self.remove_from_head()
            # self.count-=1

        self.dict[key]=node
        self.add_to_tail(node)
        # self.count+=1

cache = LRUCache( 2 )

cache.put(1, 1);

import ipdb; ipdb.set_trace()

cache.put(2, 2);

import ipdb; ipdb.set_trace()


cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2

import ipdb; ipdb.set_trace()

cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)

import ipdb; ipdb.set_trace()

cache.get(3);       # returns 3
cache.get(4);       # returns 4
