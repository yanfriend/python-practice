import collections


def preference_list(id_list):
    graph = collections.defaultdict(set)
    all_ids = set()

    for ids in id_list:
        all_ids.update(set(ids))
        for i in range(1, len(ids)):
            graph[ids[i - 1]].add(ids[i])

    in_degree = {id: 0 for id in all_ids}
    for k in graph:
        for nei in graph[k]:
            in_degree[nei] += 1

    ret = []
    qu = [id for id in in_degree if in_degree[id] == 0]
    while len(qu) > 0:
        new = []
        for node in qu:
            ret.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    new.append(nei)
        qu = new
    return ret


print preference_list([[3, 5, 7, 9], [2, 3, 8], [5, 8]])  # [2, 3, 5, 8, 7, 9]
