from timeit import default_timer as timer
from kmp_algorithm import kmp_alg, prefix_function
from naive_algorithm import naive_alg

text = "a" * 1000000000
pattern = "a" * 1000
start = timer()
naive_alg(text, pattern)
end = timer()
print(end-start)

start = timer()
kmp_alg(text, pattern, prefix_function(pattern))
end = timer()
print(end-start)
