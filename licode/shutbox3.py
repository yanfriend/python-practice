import random


def flip_tiles():
    numbers = set(i for i in range(1, 10))

    while len(numbers) > 0:
        if sum(numbers) <= 6:  # roll one dice if sum of numbers <= 6
            n1 = random.randint(1, 6)
            n2 = 0
        else:
            n1 = random.randint(1, 6)
            n2 = random.randint(1, 6)

        # n1=random.randint(1,6)
        # n2=random.randint(1,6)

        s = n1 + n2

        def find_strategies(strategies, path, number_list, ind):
            if sum(path) == s:
                strategies.append(path)
                return
            if sum(path) > s:
                return

            for i in range(ind, len(number_list)):
                find_strategies(strategies, path + [number_list[i]], number_list, i + 1)
                if len(strategies) > 0: break

        strategies = []

        find_strategies(strategies, [], sorted(list(numbers), reverse=True), 0)  # a list of trategies

        # print strategies

        if len(strategies) == 0: return False

        strategy = strategies[0]
        for s in strategy:
            numbers.remove(s)

    return True


win = lose = 0
for i in range(100000):  # 100000
    if flip_tiles():
        win += 1
    else:
        lose += 1
print win * 1.0 / (win + lose)  # 9.x%

'''
shut box numbers are 1, 2, ..9 only. 
at most three numbers can be chosen. 

NO. 1+2+3+4=10, can be four numbers.

leave open as many possibilities as possible for future rolls. 
You do this by closing as few numbers as possible on each roll. 
Closing 5 is better than closing 2 and 3 because if you roll a 2 or a 3, 
the 5 won't help you, but the 2 and 3 together can serve any purpose the 5 could serve.
'''
