class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

head.next.next.next.next.next=ListNode(6)


def reverse(head):
    # reverse in pair
    dummy=dummy_keep=ListNode(0)
    dummy.next = head

    while head and head.next:
        next=head.next.next

        tmp=head
        dummy.next=head.next
        dummy=dummy.next
        dummy.next=tmp
        dummy=dummy.next
        dummy.next=next

        head=next

    return dummy_keep.next



rl = reverse(head)
# import ipdb; ipdb.set_trace()
while rl:
    print rl.val,
    rl=rl.next

