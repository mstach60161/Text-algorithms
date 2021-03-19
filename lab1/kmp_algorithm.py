def prefix_function(pattern):
    pref_arr = [0]
    k = 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = pref_arr[k - 1]
        if pattern[k] == pattern[q]:
            k = k + 1
        pref_arr.append(k)
    return pref_arr


def kmp_alg(text, pattern, pref_arr):
    number = 0
    m = 0
    for i in range(len(text)):
        while m > 0 and pattern[m] != text[i]:
            m = pref_arr[m-1]
        if pattern[m] == text[i]:
            m += 1
        if m == len(pattern):
            number += 1
            m = pref_arr[m-1]
    return number




