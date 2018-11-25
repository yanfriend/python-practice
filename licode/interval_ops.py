def interval_and(int1, int2):
    if not int1 or not int2: return []

    i=j=0
    ret=[]
    while i<len(int1) and j<len(int2):
        if int2[j][0]<=int1[i][0]<=int2[j][1] or \
            int2[j][0]<=int1[i][1]<=int2[j][1] or \
            int1[i][0]<=int2[j][0]<=int1[i][1] or \
            int1[i][0]<=int2[j][1]<=int1[i][1]:
            new_int=[max(int1[i][0],int2[j][0]), min(int1[i][1],int2[j][1])]
            # if ret and (ret[-1][1]>=new_int[0] or ret[-1][1]+1==new_int[0]):
            #     ret[-1][1]=new_int[1]
            # else:
            #     ret.append(new_int)
            ret.append(new_int)

        if int1[i][1]>=int2[j][1]: j+=1
        else: i+=1

    return ret

int1=[[0, 2], [5, 10], [16, 20], [25, 26], [28, 30]]
int2=[[1, 5], [11, 12], [14, 18], [20, 23]]
print interval_and(int1, int2)


def interval_or(int1, int2):
    i=j=0
    ret=[]
    while i<len(int1) or j<len(int2):
        if i==len(int1):
            new_int=int2[j]; j+=1
        elif j==len(int2):
            new_int=int1[i]; j+=1
        elif int2[j][0]<=int1[i][0]<=int2[j][1] or \
            int2[j][0]<=int1[i][1]<=int2[j][1] or \
            int1[i][0]<=int2[j][0]<=int1[i][1] or \
            int1[i][0]<=int2[j][1]<=int1[i][1]:
            new_int=[min(int1[i][0],int2[j][0]), max(int1[i][1],int2[j][1])]
            i+=1; j+=1
        else:
            if int1[i][1]>=int2[j][1]: new_int=int2[j]; j+=1
            else: new_int=int1[i]; i+=1

        if ret and \
            (ret[-1][1]>=new_int[0] or ret[-1][1]+1==new_int[0]):
                ret[-1][1]=max(new_int[1], ret[-1][1])
        else: ret.append(new_int)

    return ret

int1=[[0, 2], [6, 8], [16, 20]]
int2=[[1, 5], [12, 18], [20, 23]]
print interval_or(int1, int2)

"""
[[1, 2], [5, 5], [16, 18], [20, 20]]
[[0, 8], [12, 23]]
"""
