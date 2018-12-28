import collections


def path_sum(nums):
    mp = collections.defaultdict(dict)
    max_row = 0
    for n in nums:
        row = n / 100
        pos = n % 100 / 10
        val = n % 10
        mp[row][pos] = val
        max_row = max(max_row, row)

    ans = 0
    for i in range(1, max_row):
        for k, v in mp[i].iteritems():
            if i + 1 in mp and (k - 1) * 2 + 1 in mp[i + 1]:
                mp[i + 1][(k - 1) * 2 + 1] += v
            else:
                ans += v
            if i + 1 in mp and (k - 1) * 2 + 2 in mp[i + 1]:
                mp[i + 1][(k - 1) * 2 + 2] += v
            else:
                ans += v

    return sum(mp[max_row].values()) + ans

print path_sum([113, 215, 221])

assert path_sum([113, 215, 221])==12
print 'SUCCESS'

