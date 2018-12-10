

class Solution(object):

    def set_buddy(self, my_list, buddy_list):
        self.my_list=my_list
        self.buddy_list=buddy_list

    def recommendCities(self, k):
        """:rtype a list of strings"""
        pass

    def compare(self, item1, item2):
        set1 = set(item1).intersection(self.my_list)
        set2 = set(item2).intersection(self.my_list)
        return len(set2) - len(set1)  # reversed order

    def test_sort(self):
        self.buddy_list.sort(cmp=self.compare)

        print self.buddy_list # more similar with my_list, more front in the list


"""
            # me: will skip this and only do a sort
            
            Set<String> myWishList = new HashSet<>(Arrays.asList(new String[]{"a", "b", "c", "d"}));
            Set<String> wishList1 = new HashSet<>(Arrays.asList(new String[]{"a", "b", "e", "f"}));
            Set<String> wishList2 = new HashSet<>(Arrays.asList(new String[]{"a", "c", "d", "g"}));
            Set<String> wishList3 = new HashSet<>(Arrays.asList(new String[]{"c", "f", "e", "g"}));
            Map<String, Set<String>> friendWishLists = new HashMap<>();
            friendWishLists.put("Buddy1", wishList1);
            friendWishLists.put("Buddy2", wishList2);
            friendWishLists.put("Buddy3", wishList3);
            Solution sol = new TravelBuddy().new Solution(myWishList, friendWishLists);
            List<String> res = sol.recommendCities(10);
            assertEquals(3, res.size());
            assertEquals("g", res.get(0));
            assertEquals("e", res.get(1));
assertEquals("f", res.get(2));
"""


sol = Solution()
sol.set_buddy(['a', 'b', 'c', 'd'],
              [["a", "b", "e", "f"], ["a", "c", "d", "g"], ["c", "f", "e", "g"]])

sol.test_sort()

