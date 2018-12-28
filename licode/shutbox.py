import random

# random.seed(a=None)


def play_shutbox():
    numbers = set([i for i in range(1, 10)])

    while len(numbers) > 0:

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        selected = strategy(numbers, d1 + d2)
        if len(selected) == 0: return False
        numbers -= set(selected)

    return True


def strategy(numbers, target):
    if target in numbers: return [target]

    cnt=0
    for i in sorted(numbers):
        # if i in (4,5,6): continue

        if target - i in numbers:
            # if cnt==0: cnt+=1; continue # not help
            return [i, target - i]


    for i in sorted(numbers):
        if target - i in numbers:
            return [i, target - i]

    return []


success, failure = 0, 0
for i in range(10000):
    if play_shutbox():
        success += 1
    else:
        failure += 1
print success / float(success + failure)
