def menu_order(inp, target):
    eps = 10 ** -6  # error 1, if use 1**-6, it's 1

    prices = [(v,k) for k,v in inp.items()]

    ret = []

    def helper(index, path, sumup):
        if abs(sumup - target) <= eps:
            ret.append(path)
            return
        elif sumup - target > eps:  # error 2, miss this ending condition
            return

        if index >= len(prices): return

        for i in range(index, len(prices)):
            helper(i, path + [prices[i][1]], sumup + prices[i][0])

    helper(0, [], 0)
    return ret


# print menu_order({"dish1":2.40, 0.01, 6.00, 2.58], 2.50)

print menu_order({'dish1':2, 'dish1-1':2, 'dish2':3, 'dish3':5, 'dish4':8}, 10)
'''
[[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 3, 5], [2, 8], [5, 5]]
[
['dish1', 'dish1', 'dish1', 'dish1', 'dish1'], 
['dish1', 'dish1', 'dish1', 'dish1', 'dish1-1'], 
['dish1', 'dish1', 'dish1', 'dish1-1', 'dish1-1'], 
['dish1', 'dish1', 'dish1-1', 'dish1-1', 'dish1-1'], 
['dish1', 'dish1-1', 'dish1-1', 'dish1-1', 'dish1-1'],
['dish1-1', 'dish1-1', 'dish1-1', 'dish1-1', 'dish1-1'], 

['dish1', 'dish1', 'dish2', 'dish2'], 
['dish1', 'dish1-1', 'dish2', 'dish2'],
['dish1-1', 'dish1-1', 'dish2', 'dish2'],
 
['dish1', 'dish3', 'dish2'], 
['dish1-1', 'dish3', 'dish2'],

['dish1', 'dish4'],  
['dish1-1', 'dish4'],
 
['dish3', 'dish3']]
'''

# print menu_order([5, 3, 2, 8], 10)
#
# print menu_order([1, 2, 3, 4, 5], 9)
#
# print menu_order([1, 2, 3, 4, 5], -9)
