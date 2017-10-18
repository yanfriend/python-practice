# http://1point3acres.com/bbs/thread-235593-1-1.html

def can_drive(shifts, current_time):
    driving=rest=0
    shifts.insert(0,[0,0])

    for i in range(1, len(shifts)):
        if current_time<=shifts[i][0]:
            break
        elif current_time<=shifts[i][1]:
            shifts[i][1]=current_time

        rest = shifts[i][0]-shifts[i-1][1]
        if rest>=8:
            driving=0

        driving += shifts[i][1]-shifts[i][0]
        if driving>=12: return False

    return True

print can_drive([[0,8], [10,12], [25,33]],33) # true
print can_drive([[9, 10], [12, 22]],24) # true

print can_drive([[9, 10], [12, 23]],24) # False
print can_drive([[0, 4], [5, 9], [10, 14], [15, 19], [20, 24]],24) # false
print can_drive([[0, 4], [5, 9], [10, 14], [15, 19], [20, 24]],13) # true

