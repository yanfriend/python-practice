
# def test_nested_func():
#     ans=8
#
#     def inner():
#         ans += 1 # this does not work if not in a class
#         print ans
#
#     inner()
#     return ans
#
# print test_nested_func()


class Solution(object):

    def test_nested_func(self):
        self.ans = 8

        def inner():
            self.ans += 1
            print self.ans

        inner()
        return self.ans

# print test_nested_func()

print Solution().test_nested_func()
