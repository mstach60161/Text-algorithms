def naive_alg(text, pattern):
    number = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if pattern == text[i: i + len(pattern)]:
            number += 1
    return number


naive_alg("abcabcabcabc", "abc")



