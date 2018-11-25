def verify_preorder(pre_order):
    st=[]
    last_min=float('-inf')

    for pre in pre_order:
        if pre<last_min: return False
        while st and pre>st[-1]: # st maintains descreasing.
            last_min=st.pop()
        st.append(pre)

    return True

print verify_preorder([5, 2, 1, 3, 6])

print verify_preorder([10,8,5,9,15,16])

print verify_preorder([10,8,5,9,15,16,14])

"""
True
True
False
"""

"""
use pre_order list instead of stack to save space.

class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        int low = INT_MIN, i = -1;
        for (auto a : preorder) {
            if (a < low) return false;
            while (i >= 0 && a > preorder[i]) {
                low = preorder[i--];
            }
            preorder[++i] = a;
        }
        return true;
    }
};
"""
