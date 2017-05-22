# Python program to do inorder traversal without recursion and
# without stack Morris inOrder Traversal

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative function for inorder tree traversal
def MorrisTraversal(root):

    # Set current to root of binary tree
    current = root

    while current is not None:

        if current.left is None:
            print current.data ,
            current = current.right
        else:
            #Find the inorder predecessor of current
            prev=current

            current = current.left
            while(current.right is not None and current.right != prev):
                current = current.right

            # Make current as right child of its inorder predecessor
            if current.right is None:
                current.right = prev
                current = prev.left

            # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecssor
            else:
                current.right = None
                print prev.data ,
                current = prev.right

# Driver program to test above function
"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

MorrisTraversal(root)

# This code is contributed by Naveen Aili
