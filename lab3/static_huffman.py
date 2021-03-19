from bitarray import bitarray
import time
import os
from bitarray._bitarray import _bitarray


class bitarray(_bitarray):
    def __hash__(self):
        return self.tobytes().__hash__()


class Node:
    def __init__(self, sign, weight):
        self.left = None
        self.right = None
        self.sign = sign
        self.weight = weight


def create_tree(element1, weight, element2):
    root = Node("#", weight)
    root.left = element1
    root.right = element2
    return root


def hashing_rec(head, code, key):
    if head.sign is not "#":
        code[head.sign] = key
    if head.left is not None:
        hashing_rec(head.left, code, key + bitarray('0'))
    if head.right is not None:
        hashing_rec(head.right, code, key + bitarray('1'))


def hashing(head):
    code = {}
    hashing_rec(head, code, bitarray(''))
    return code


def huffman(letter_counts):
    nodes = []
    for a, weight in letter_counts.items():
        nodes.append(Node(a, weight))
    internal_nodes = []
    leafs = sorted(nodes, key=lambda n: n.weight)
    while len(leafs) + len(internal_nodes) > 1:
        head = []
        internal_nodes = [i for i in internal_nodes if i]
        if len(leafs) >= 2:
            head += leafs[:2]
        elif len(leafs) == 1:
            head += leafs[:1]
        if len(internal_nodes) >= 2:
            head += internal_nodes[:2]
        elif len(internal_nodes) == 1:
            head += internal_nodes[:1]
        head.sort(key=lambda n: n.weight)
        element_1, element_2 = head[:2]
        internal_nodes.append(create_tree(element_1, element_1.weight + element_2.weight, element_2))
        if len(leafs) > 0 and element_1 == leafs[0]:
            leafs = leafs[1:]
        else:
            internal_nodes = internal_nodes[1:]
        if len(leafs) > 0 and element_2 == leafs[0]:
            leafs = leafs[1:]
        else:
            internal_nodes = internal_nodes[1:]
    return internal_nodes[0]


def counting(text):
    letters = {}
    for sign in text:
        if sign in letters:
            letters[sign] = letters[sign] + 1
        else:
            letters[sign] = 1
    return letters


def from_bits_to_letters(code):
    dictionary = {}
    for key in code:
        dictionary[code[key]] = key
    return dictionary





def compress(path1, path2):
    start = time.time()
    with open(path1, 'r') as file:
        text = file.read()
        file.close()
        code = hashing(huffman(counting(text)))
        array = bitarray('')
        for sign in text:
            array = array + code[sign]
    with open(path2, 'wb') as compressed:
        compressed.write(array)
        compressed.close()
    end = time.time()
    print("Before compression: ", os.stat(path1).st_size, "b")
    print("After compression: ", os.stat(path2).st_size, "b")
    print("Compression ratio: ", 100 * os.stat(path2).st_size / os.stat(path1).st_size, "%")
    print("Compression time: ", end - start)
    return code, array.length()


def decompress(path1, path2, size, code):
    start = time.time()
    decode = from_bits_to_letters(code)
    with open(path1, 'rb') as file:
        array = bitarray()
        byte = file.read()
        file.close()
        array.frombytes(byte)
        array = array[:-(array.length() - size)]
        buff = bitarray()
        string = ""
        for sign in array:
            if sign is False:
                buff = buff + bitarray('0')
            else:
                buff = buff + bitarray('1')
            if buff in decode:
                string = string + decode[buff]
                buff = bitarray()
    with open(path2, 'w') as result:
        result.write(string)
        result.close()
    end = time.time()
    print("Before decompression: ", os.stat(path1).st_size, "b")
    print("After decompression: ", os.stat(path2).st_size, "b")
    print("Decompression time: ", end - start)


print("1 KB FILE")
code, size = compress("file1.txt", "binfile1.bin")
decompress("binfile1.bin", "file2_1.txt", size, code)
print()
print("10 KB FILE")
code, size = compress("file10.txt", "binfile10.bin")
decompress("binfile10.bin", "file2_10.txt", size, code)
print()
print("100 KB FILE")
code, size = compress("file100.txt", "binfile100.bin")
decompress("binfile100.bin", "file2_100.txt", size, code)
print()
print("1000 KB FILE")
code, size = compress("file1000.txt", "binfile1000.bin")
decompress("binfile1000.bin", "file2_1000.txt", size, code)
