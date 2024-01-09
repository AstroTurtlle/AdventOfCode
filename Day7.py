import functools
def check_type(hand):
    hand = list(hand)
    freq = {}
    #Make a frequency list
    for i in range(5):
        if not hand[i] in freq.keys():
            freq[hand[i]] = 1
        else:
            freq[hand[i]] += 1
    val = freq.values()
    #Start of additional code for part2
    k = freq.keys()
    if not 'J' in k:
        pass
    else:
        if freq['J'] == 5:
            return 6
        nr_jokers = freq['J']
        freq.pop('J')
        val = freq.values()
        val = sorted(val)
        val[-1] += nr_jokers
    #End of additional code for part2
    if 5 in val:
        return 6
    if 4 in val:
        return 5
    if 3 in val:
        if 2 in val:
            return 4
        return 3
    if 2 in val:
        if len(val) == 3:
            return 2
        return 1
    return 0

def poker_cmp(hand1,hand2):
    hand1 = list(hand1.split()[0])
    hand2 = list(hand2.split()[0])
    order = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    for i in range(len(hand1)):
        if order.index(hand1[i]) == order.index(hand2[i]):
            continue
        elif order.index(hand1[i]) > order.index(hand2[i]):
            return 1
        return -1
    return 0

def citire(filename):
    with open(filename) as f:
        lines = f.readlines()
        s = 0
        types = [[], [], [], [], [], [], []]
        rank = 1
        for line in lines:
            hand = line.split()[0]
            hand_type = check_type(hand)
            types[hand_type].append(line[:-1])
        for i in range(len(types)):
            types[i] = sorted(types[i], key=functools.cmp_to_key(poker_cmp))
            for j in types[i]:
                bid = int(j.split()[1])
                s += rank * bid
                rank += 1
    return s

print(citire('input.txt'))