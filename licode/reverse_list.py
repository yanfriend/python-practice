class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None

def reverse_list(root):
    prev=None
    curr=root
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev


root=Node(0)
root.next=Node(1)
root.next.next=Node(2)
root.next.next.next=Node(3)

reversed=reverse_list(root)

while reversed:
    print reversed.val
    reversed=reversed.next
