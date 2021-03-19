import os
import time
import objsize
from dbf import kmr, find_dbf
from kmp_algorithm import kmp_alg
from suffix_tree import SuffixTree

files = ("1997_714.txt", "romeo-i-julia-700.txt", "zad6.txt")
functions = {"kmr": kmr, "SuffixTree": SuffixTree}
patterns = ("e", "Te psy", "Oto nadchodzi jeden z krewnych")

for path in files:
    with open(path, 'r') as file:
        text = file.read()
        for func in functions.keys():
            start_time = time.time()
            functions[func](text)
            end_time = time.time()

            print("text", path)
            print("function", func)
            print("time:", end_time - start_time, "\n")


for path in files:
    with open(path, 'r') as file:
        text = file.read()
        dbf_dic = kmr(text)

        print("text:", path)
        print("file size:", os.stat(path).st_size)
        print("dbf dictionary size:", objsize.get_deep_size(dbf_dic), "\n")

path = files[1]
text = open(path, 'r').read()

for pattern in patterns:
    start_time = time.time()
    kmp_res = kmp_alg(text, pattern)
    end_time = time.time()
    kmp_time = end_time - start_time

    start_time = time.time()
    names, entries = kmr(text)
    dbf_res = find_dbf(text, pattern, names, entries)
    end_time = time.time()
    dbf_with_dict = end_time - start_time

    start_time = time.time()
    find_dbf(text, pattern, names, entries)
    end_time = time.time()
    dbf = end_time - start_time

    print("text:", path)
    print("pattern:", pattern)
    print("kmp time:", kmp_time)
    print("dbf and dictionary time:", dbf_with_dict)
    print("dbf time:", dbf)
    print("kmp result: ", kmp_res)
    print("dbf result:", dbf_res, "\n")
