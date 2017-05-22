"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ? m ? n ? length of list.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dummy=dummy_keep=ListNode(0)
        dummy.next=head

        for i in range(m-1):
            dummy=dummy.next

        # prt(dummy)

        prev=dummy; curr=dummy.next
        for i in range(m,n+1):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        # 1->2<-3<-4 5->null to 1->2->5, 2<-3<-4 to 1->4->3->2 -> 5

        dummy.next.next=curr
        dummy.next=prev

        prt(dummy_keep.next)

        return dummy_keep.next


def prt(head):
    while head:
        print head.val,
        head=head.next

lst=ListNode(1)
lst.next=ListNode(2)
lst.next.next=ListNode(3)
lst.next.next.next=ListNode(4)
lst.next.next.next.next=ListNode(5)

# prt(lst)
Solution().reverseBetween(lst, 2, 4)
