import random

mp=set()

def flip_tiles():
    numbers=set(i for i in range(1,10))

    s=0
    while len(numbers)>0:
        if sum(numbers)<=6: # roll one dice if sum of numbers <= 6
            n1=random.randint(1,6)
            n2=0
        else:
            n1=random.randint(1,6)
            n2=random.randint(1,6)

        s=n1+n2

        if s in numbers:
            numbers.remove(s)
            continue

        found = False
        sorted_numbers=sorted(numbers)
        for n1 in sorted_numbers: # error 1, need +1 to use s/2
            n2=s-n1
            if n1>=n2: continue

            if n2 in numbers:
                numbers.remove(n1)
                numbers.remove(n2)
                found=True
                break

        if found: continue

        # try three numbers
        if len(numbers)<3: return False

        for i, n1 in enumerate(sorted_numbers):
            if found:
                break;
            for j in range(i+1, len(sorted_numbers)):
                n2=sorted_numbers[j]
                n3=s-n1-n2
                if n3 not in numbers or n3==n1 or n3==n2:
                    continue
                numbers.remove(n1)
                numbers.remove(n2)
                numbers.remove(n3)
                found=True
                break
        if found: continue
        else: return False

    mp.add(s) # s is true
    return True

win=lose=0
for i in range(100000):
    if flip_tiles():
        win+=1
    else:
        lose+=1
print win*1.0/(win+lose)  # 9.x%
# print mp  # set([8, 1, 10, 4, 2])

'''
shut box numbers are 1, 2, ..9 only. 
at most three numbers can be chosen. 

1+2+3+4=10, can be four numbers.
'''
