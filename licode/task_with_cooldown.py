# def cooldown(tasks, cool):
#     # para check
#     ret=0
#     task_start={}
#     qu=[]
#     for i,t in enumerate(tasks):
#         start_ind=task_start.get(t,-cool-1)
#         while len(qu)-1-start_ind<cool:
#             qu.append(-1)
#         qu.append(t)
#         task_start[t]=len(qu)-1
#     print qu
#     return len(qu)


def cooldown(tasks, cool):
    # para check
    ret=0
    task_start={}
    for i,t in enumerate(tasks):
        start_ind=task_start.get(t,None)

        if not start_ind or ret-start_ind>cool:
            ret+=1
            task_start[t]=ret
        else:
            ret+=cool+1-(ret-start_ind)
            task_start[t]=ret
    return ret

print cooldown([1,1,2,1],2) # 7
print cooldown([1,2,3,1,2,3],3) # 7
print cooldown([1,2,3,4,5,6,2,4,6,1,2,4],6) #18
