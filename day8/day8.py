ops = {
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b,
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '!=': lambda a, b: a != b,
    '==': lambda a, b: a == b,
}


def parse(line):
    splat = line.split(' ')
    assert len(splat) == 7
    reg1, op1name, val1, _, reg2, op2name, val2 = splat
    val1, val2 = int(val1), int(val2)
    if op1name == "dec":
        val1 *= -1
    op2 = lambda x: ops[op2name](x, val2)

    return reg1, val1, reg2, op2


def runLines(data):
    maxSeen = 0

    comp = computer()
    for line in data:
        chReg, amt, checkReg, cond = parse(line)
        if cond(comp.value(checkReg)):
            comp.add(chReg, amt)
            maxSeen = max(maxSeen, comp.maxRegisterValue())

    return comp, maxSeen


class computer:

    def __init__(self):
        self.registers = dict()

    def value(self, regname):
        if regname in self.registers:
            return self.registers[regname]

        self.registers[regname] = 0
        return 0

    def add(self, regname, amount):
        if regname in self.registers:
            self.registers[regname] += amount
            return
        self.registers[regname] = amount

    def maxRegisterValue(self):
        return max(self.registers.values())


data = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''.split('\n')
comp, maxSeen = runLines(data)
assert comp.maxRegisterValue() == 1
assert maxSeen == 10


with open('day8.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]
comp, maxSeen = runLines(data)
assert comp.maxRegisterValue() == 4416
assert maxSeen == 5199
