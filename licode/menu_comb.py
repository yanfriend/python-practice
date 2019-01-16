"""
Given a menu (list of items prices),
find all possible combinations of items that sum a particular value K.
"""


def menu_items(menus, K):  # can order multiple times of one item
    ret = []

    def helper(path, sumup, index):
        if sumup == K:
            ret.append(path)
            return
        elif sumup > K:
            return

        for i in range(index, len(menus)):
            helper(path + [menus[i]], sumup + menus[i], i)

    helper([], 0, 0)
    return ret
    # return min([len(i) for i in ret]) # shortest length

# print menu_items([2, 3, 5, 8], 10)
# print menu_items([5, 3, 2, 8], 10)

print menu_items([1, 2, 3, 4, 5],9)
