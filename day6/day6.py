def keyFn(state):
    return ';'.join((str(x) for x in state))


def maxI(state):
    target = max(state)
    for i, x in enumerate(state):
        if x == target:
            return i, x


def redistribute(state):
    killIdx, size = maxI(state)
    state[killIdx] -= size
    i = killIdx + 1
    while size > 0:
        if i >= len(state):
            i %= len(state)
        state[i] += 1
        i += 1
        size -= 1


def count(data):
    seen = set()
    this = keyFn(data)

    i = 0
    while this not in seen:
        i += 1
        seen.add(this)
        redistribute(data)
        this = keyFn(data)

    return i


assert count([0, 2, 7, 0]) == 5

with open('day6.txt', 'r') as f:
    data = [int(x) for x in f.read().strip().split('\t')]

print count(data)
