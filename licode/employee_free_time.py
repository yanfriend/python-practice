def get_free_time(schedule):
    # schedule is list of list, ignore here, should flat out first.
    schedule.sort(key=lambda x:x[0])

    res=[]
    itv = schedule[0]

    for i in range(1, len(schedule)):
        if itv[1]<schedule[i][0]:
            res.append([itv[1], schedule[i][0]])

        itv[1]=max(itv[1], schedule[i][1])

    return res

schedule = [[1,2],[5,6],[1,3],[4,10]]
print get_free_time(schedule)

schedule = [[1,3],[6,7],[2,4],[2,5],[9,12]]
print get_free_time(schedule)


"""
Input: schedule = [[1,2],[5,6],[1,3]],[[4,10]]
Output: [[3,4]]

schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
"""
