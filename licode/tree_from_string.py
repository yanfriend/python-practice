class Node(object):
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def binary_tree_from_string(s):
    if not s: return None

    node=Node(int(s[0]))

    i=2; cnt=1
    while cnt>0 and i<len(s):
        if s[i]=='(': cnt+=1
        elif s[i]==')': cnt-=1
        i+=1

    node.left=binary_tree_from_string(s[2:i]) # remove () and recursively call
    node.right=binary_tree_from_string(s[i+1:-1])
    return node



tree = binary_tree_from_string('4(2(3)(1))(6(5))')  # suppose only single digits.
print tree