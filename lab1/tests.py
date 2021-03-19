
from timeit import default_timer as timer
from kmp_algorithm import kmp_alg
import kmp_algorithm
from naive_algorithm import naive_alg


print("Ustawa:")
with open("1997_714file.txt", errors='ignore') as file:
    start = timer()
    number = 0
    pattern = "art"
    pref_arr = kmp_algorithm.prefix_function(pattern)
    for line in file:
        number += kmp_alg(line, pattern, pref_arr)
    end = timer()
    print("kmp_alogithm time: ", ("%.6f" % (end - start)), "s")
print(number)
with open("1997_714file.txt", errors='ignore') as file:
    start = timer()
    number = 0
    for line in file:
        number += naive_alg(line, pattern)
    end = timer()
    print("naive time: ", ("%.6f" % (end - start)), "s")

print("Wikipedia:")
with open("s118Rd3YIR6j.txt", errors='ignore') as file:
    start = timer()
    number = 0
    pattern = "kruszwil"
    pref_arr = kmp_algorithm.prefix_function(pattern)
    for line in file:
        number += kmp_alg(line, pattern, pref_arr)
    end = timer()
    print("kmp_alogithm time: ", ("%.6f" % (end - start)), "s")

with open("s118Rd3YIR6j.txt", errors='ignore') as file:
    start = timer()
    number = 0
    for line in file:
        number += naive_alg(line, pattern)
    end = timer()
    print("naive time: ", ("%.6f" % (end - start)), "s")







