# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return

        slow=fast=prev=head
        while fast:
            prev=slow
            slow=slow.next
            if not fast.next: break
            fast=fast.next.next

        p1=head; p2=slow
        prev.next=None

        # reverse p2
        curr=p2
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        p2=prev

        while p1:
            tmp=p1.next
            p1.next=p2
            p1=p1.next
            p2=tmp

    def merger(self,p1,p2):
        keep=p1
        while p1:
            import ipdb;ipdb.set_trace()

            tmp=p1.next
            p1.next=p2
            p1=p1.next
            p2=tmp
        return keep

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)

# Solution().reorderList(head)
# ll=head


p1=ListNode(1)
p1.next=ListNode(2)
# p1.next.next.next=ListNode(4) # not work with this

p2=ListNode(11)

ll=Solution().merger(p1,p2)

while ll:
    print ll.val,
    ll=ll.next
