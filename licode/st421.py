class Solution(object):

    class Trie(object):
        def __init__(self):
            self.children=[None, None]

    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # create Trie.
        trie=Solution.Trie()
        for num in nums:
            curr=trie
            for i in range(32)[::-1]:
                if not curr.children[num>>i&1]:
                    curr.children[num>>i&1]=Solution.Trie()
                curr=curr.children[num>>i&1]

        # go through trie, find max corresponding xor possible.
        ret=0
        for num in nums:
            curr=trie
            part_sum=0

            for i in range(32)[::-1]:
                if curr.children[((num>>i)^1)&1]:
                    part_sum|=1<<i
                    curr=curr.children[((num>>i)^1)&1]
                else:
                    curr=curr.children[(num>>i)&1]
                ret=max(ret, part_sum)

        return ret

