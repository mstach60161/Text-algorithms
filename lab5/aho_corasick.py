from pip._vendor.msgpack.fallback import xrange


class AhcNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None


def create_trie(patterns):
    root = AhcNode()

    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhcNode())
        node.out.append(path)
    return root


def ahc_create_statemachine(patterns):
    root = create_trie(patterns)
    queue = []
    for node in root.goto.values():
        queue.append(node)
        node.fail = root

    while len(queue) > 0:
        rnode = queue.pop(0)

        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and not fnode.goto.__contains__(key):
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out

    return root


def ahc_find(text, root, patterns):
    node = root
    dictionary = {}
    for pattern in patterns:
        dictionary[pattern] = []
    for i in xrange(len(text)):
        while node is not None and text[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[text[i]]
        for pattern in node.out:
            #print("at poisition", i - len(pattern) + 1, "found", pattern)
            dictionary[pattern].append(i-len(pattern)+1)
    return dictionary


patterns = ['a', 'ab', 'abc', 'bc', 'c']
text = "abcbaadbvbcvv"
root = ahc_create_statemachine(patterns)
d = ahc_find(text, root, patterns)


