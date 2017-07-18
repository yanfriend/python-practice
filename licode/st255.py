class Solution:
    # @param {integer[]} inorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        return self.helper(preorder, 0, len(preorder)-1)

    def helper(self,preorder, start, end):
        if start>=end: return True
        pivot=preorder[start]
        i=start+1
        while i<=end:
            if preorder[i]>pivot: break
            i+=1
        pi=i
        while i<=end:
            if preorder[i]<pivot: break
            i+=1
        if i!=end+1: return False
        return self.helper(preorder,start+1,pi-1) and self.helper(preorder,pi,end)

print Solution().verifyPreorder([5,3,1,4,8,7,12])

"""
class Solution {
public:
    bool verifyPreorder(vector<int>& inorder) {
        int low = INT_MIN;
        stack<int> s;
        for (auto a : inorder) {
            if (a < low) return false;
            while (!s.empty() && a > s.top()) {
                low = s.top(); s.pop();
            }
            s.push(a);
        }
        return true;
    }
};

class Solution {
public:
    bool verifyPreorder(vector<int>& inorder) {
        int low = INT_MIN, i = -1;
        for (auto a : inorder) {
            if (a < low) return false;
            while (i >= 0 && a > inorder[i]) {
                low = inorder[i--];
            }
            inorder[++i] = a;
        }
        return true;
    }
};
"""
