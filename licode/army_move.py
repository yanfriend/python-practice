import collections


def battle(inp):
    city_armies = collections.defaultdict(set)
    army_strength = collections.defaultdict(int)
    ret=dict()

    for line in inp:
        items = line.split(' ')
        army_strength[items[0]]=1

        action=items[2]
        if action == 'Move':
            city_armies[items[3]].add(items[0])
        elif action in ['Hold', 'Support']:
            city_armies[items[1]].add(items[0])

    for line in inp:
        items = line.split(' ')
        if items[2]=='Support':
            if len(city_armies[items[1]])==1: # no one attach it
                army_strength[items[3]] += 1

    for city, armies in city_armies.items():
        if len(armies)==1:
            ret[armies.pop()] = city
        else:
            max_val = 0
            win = ''
            for a in armies:
                if army_strength[a] > max_val:
                    if win:
                        ret[win]='Dead'
                    max_val = army_strength[a]
                    win=a
                    ret[a]=city
                elif army_strength[a]==max_val:
                    ret[a]='Dead'
                    ret[win]='Dead'
                elif army_strength[a] < max_val:
                    ret[a]='Dead'

    return ret


input=[
"A Mu Hold",
"B Bohemia Move Mu",
"C Pru Move Mu",
"D war Hold"] # {'A': 'Dead', 'C': 'Dead', 'B': 'Dead', 'D': 'war'}

input=[
    "D XX Hold",
    "B Bo Move Mu",
    "C DF Support B",
    "M Wa Support B",
    "G FC Move Mu",
    "F dd Support G"]

input=[
"A Mu Hold",
"B Bo Move Mu",
"C Wa Support B"] # {'A': 'Dead', 'C': 'Wa', 'B': 'Mu'}

print battle(input)
