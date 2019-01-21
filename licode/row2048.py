
def remove_letters(lst, val):
    ind=0
    for ele in lst:
        if ele!=val:
            lst[ind]=ele
            ind+=1
    for i in range(ind,len(lst)):
        lst[i]=-1

def left_move(row):
    remove_letters(row, -1)

    for i in range(len(row)-1):
        if row[i]==-1: continue
        if row[i]==row[i+1]:
            row[i]*=2
            row[i+1]=-1

    remove_letters(row, -1)
    print row

print left_move([2,4,-1,4,2,8,8,-1,-1])