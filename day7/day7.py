class tree:

    def __init__(self, treeNodes):
        self.__nodes = treeNodes
        self.setRoot()

    def root(self):
        return self.__root

    def setRoot(self):
        start = self.__nodes.keys()[0]
        node = self.__nodes[start]
        while node.parent() != None:
            node = node.parent()
        self.__root = node


class treeNode:

    def kids(self):
        return self.__kids

    def name(self):
        return self.__name

    def parent(self):
        return self.__parent

    def __init__(self, nameStr):
        nameData = nameStr.split(' ')
        self.__name = nameData[0]
        self.__weight = int(nameData[1].strip('()'))
        self.__kidnames = []
        self.__kids = []
        self.__parent = None

    def unbalancedSubtree(self, weight):
        if len(self.__kids) == 0:
            return weight

        ct = dict()
        for w in [x.subtreeWeight() for x in self.kids()]:
            if w not in ct:
                ct[w] = 0
            ct[w] += 1

        if len(ct.keys()) == 1:
            only = ct.keys()[0]
            return weight - (ct[only] * only)

        freqs = ct.keys()
        freqs.sort(key=lambda x: ct[x])
        oddWeight, evenWeight = freqs[0], freqs[1]
        for x in self.kids():
            if x.subtreeWeight() == oddWeight:
                return x.unbalancedSubtree(evenWeight)

    def subtreeWeight(self):
        if len(self.__kids) == 0:
            return self.__weight
        return self.__weight + sum((x.subtreeWeight() for x in self.__kids))

    def setParent(self, parent):
        self.__parent = parent

    def setKidsNames(self, kidStr):
        self.__kidnames = [x.strip() for x in kidStr.split(',')]

    def setKidsFrom(self, coll):
        self.__kids = []
        for kidname in self.__kidnames:
            kid = coll[kidname]
            kid.setParent(self)
            self.__kids.append(kid)

    def __str__(self):
        name = "name:%s\tweight:%d" % (self.__name, self.__weight)
        kids = "" if self.__kidnames is None else "\nkids:" + \
            str(self.__kidnames)
        return name + kids


def build(data):
    coll = dict()

    for d in data:
        nodeData = d.split('->')
        jim = treeNode(nodeData[0])
        if len(nodeData) > 1:
            jim.setKidsNames(nodeData[1])
        coll[jim.name()] = jim

    for x in coll:
        coll[x].setKidsFrom(coll)

    return tree(coll)


exdata = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''.split('\n')

extree = build(exdata)
assert extree.root().name() == 'tknk'
assert extree.root().unbalancedSubtree(0) == 60


with open('day7.txt', 'r') as f:
    data = [x.strip() for x in f]
tree = build(data)
assert tree.root().name() == 'vvsvez'
assert tree.root().unbalancedSubtree(0) == 362
