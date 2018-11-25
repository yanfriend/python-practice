# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return

        last_head=root
        while last_head:

            dummy=TreeLinkNode(0)
            prev=dummy

            curr=last_head
            while curr:
                if curr.left:
                    prev.next=curr.left
                    prev=prev.next
                if curr.right:
                    prev.next=curr.right
                    prev=prev.next
                curr=curr.next

            last_head=dummy.next
