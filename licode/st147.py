"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def insertionSortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head: return head
#
#         dummy_keep=dummy=ListNode(0)
#         dummy.next=head
#
#         curr=head.next
#         prev=head
#
#         while curr:
#             import ipdb; ipdb.set_trace()
#
#             dummy=dummy_keep
#             next=curr.next
#             while dummy.next!=curr and dummy.next.val<curr.val:
#                 dummy=dummy.next
#
#             if dummy.next!=curr:
#                 curr.next=dummy.next
#                 dummy.next=curr
#                 prev.next=next
#             else:
#                 prev=prev.next
#             curr=next
#
#         return dummy_keep.next



class Solution(object):
    def insertionSortList(self, head):
        helper = ListNode(0)  # helper does not connect to head, it is like a new list
        current = head
        while current:

            pre = helper
            while pre.next and pre.next.val < current.val:
                pre = pre.next

            next = current.next

            current.next = pre.next  # the two, is to, insert current before pre.
            pre.next = current

            current = next

        return helper.next


head=ListNode(3)
head.next=ListNode(2)
head.next.next=ListNode(1)

ll=Solution().insertionSortList(head)

while ll:
    print ll.val,
    ll=ll.next



""" Read:

public class Solution {
public ListNode insertionSortList(ListNode head) {
    ListNode helper=new ListNode(0);
    ListNode pre=helper;
    ListNode current=head;
    while(current!=null) {
        pre=helper;
        while(pre.next!=null&&pre.next.val<current.val) {
            pre=pre.next;
        }
        ListNode next=current.next;
        current.next=pre.next;
        pre.next=current;
        current=next;
    }
    return helper.next;
}
"""
