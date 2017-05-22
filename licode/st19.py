# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        org=ListNode(0) # must have a fake header.
        org.next=head
        keep=org
        for i in range(n):
            head=head.next

        while head is not None:
            head=head.next
            org=org.next
        org.next=org.next.next

        return keep.next
