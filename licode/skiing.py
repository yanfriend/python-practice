import collections


def max_rewards(costs_list, rewards_list, start, ends):
    costs = collections.defaultdict(dict)
    for cl in costs_list:
        costs[cl[0]][cl[2]] = cl[1]

    rewards = {}
    earned = {}
    for p in rewards_list:
        rewards[p[0]] = p[1]
        earned[p[0]] = float('-inf')
    earned[start] = 0

    parent = {}
    q = [start]
    while len(q) > 0:
        node = q.pop()
        for nei, cost in costs[node].items():
            nei_earned = earned[node] + (rewards[nei] - cost)
            if nei_earned > earned[nei]:
                earned[nei] = nei_earned
                parent[nei] = node
                q.append(nei)

    def convert_path():
        max_earned, max_node = max([(earned[node], node) for node in ends])
        ret = []
        while max_node in parent:
            ret.append(max_node)
            max_node = parent[max_node]
        ret.append(start)
        return ret[::-1]

    return convert_path()


print max_rewards([
    ["start", 3, "A"], ["A", 4, "B"], ["B", 5, "END1"], ['start', 1, 'C'], ['C', 2, 'END1']],
    [["A", 5], ["B", 6], ["END1", 3], ['C', 100]],
    "start",
    ["END1"])
