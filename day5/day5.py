def steps(data):
    steps, head = 0, 0
    while head < len(data):
        offset = data[head]
        data[head] += 1
        head += offset
        steps += 1
    return steps


assert steps([0, 3, 0, 1, -3]) == 5

with open('day5.txt', 'r') as f:
    data = [int(x.strip()) for x in f.readlines()]

print steps(data)
