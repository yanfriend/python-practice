class ListNode(object):
    def __init__(self,val):
        self.next=None
        self.val=val

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return

        prev=fast=slow=head
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
            if fast:
                fast=fast.next

        prev.next=None
        p1=head; p2=slow

        prev=None
        while p2:
            tmp=p2.next
            p2.next=prev
            prev=p2
            p2=tmp
        p2=prev

        while p1:
            tmp=p1.next
            p1.next=p2
            p1=p1.next
            p2=tmp

        return


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)
head.next.next.next.next.next.next=ListNode(7)

Solution().reorderList(head)

while head:
    print head.val,
    head=head.next

