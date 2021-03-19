
def match_to_class(text, pattern, text_index, pat_index):
    if pattern[pat_index] == '[':
        first_ind = pat_index
        last_ind = pat_index
        while pattern[last_ind] != ']':
            last_ind += 1
    else:
        first_ind = pat_index
        last_ind = pat_index
        while pattern[first_ind] != '[':
            first_ind -= 1
    regex_class = pattern[first_ind:last_ind+1]

    matching = False
    sign = text[text_index]
    if regex_class == '[\d]':
        if '0' <= sign <= '9':
            matching = True
    if regex_class == '[\w]':
        if 'a' <= sign <= 'z' or 'A' <= sign <= 'Z':
            matching = True
    # posiblity to create own classes

    return matching, last_ind



def pattern_matching(text, pattern, text_index=0, pat_index=0):
    if text_index >= len(text):
        if pat_index >= len(pattern):
            return True
        else:
            if pat_index+1 < len(pattern) and pattern[pat_index+1] in ['*', '?']:
                return pattern_matching(text, pattern, text_index, pat_index + 2)
            else:
                return False

    elif pat_index >= len(pattern):
        return False

    if pattern[pat_index] == '[' or pattern[pat_index] == ']':
        class_matching, pat_index = match_to_class(text, pattern, text_index, pat_index)
    else:
        class_matching = False

    if pat_index+1 < len(pattern):
        if pattern[pat_index+1] == '*':
            if pattern[pat_index] == '.' or text[text_index] == pattern[pat_index] or class_matching == True:
                return pattern_matching(text, pattern, text_index, pat_index+2) \
                        or pattern_matching(text, pattern, text_index+1, pat_index)
            else:
                return pattern_matching(text, pattern, text_index, pat_index+2)

        elif pattern[pat_index+1] == '+':
            pattern = pattern[:pat_index+1] + '*' + pattern[pat_index+2:]
            if pattern[pat_index] == '.' or text[text_index] == pattern[pat_index] or class_matching == True:
                return pattern_matching(text, pattern, text_index+1, pat_index)
            else:
                return False

        elif pattern[pat_index+1] == '?':
            if pattern[pat_index] == '.' or text[text_index] == pattern[pat_index] or class_matching == True:
                return pattern_matching(text, pattern, text_index, pat_index+2) \
                        or pattern_matching(text, pattern, text_index+1, pat_index+2)
            else:
                return pattern_matching(text, pattern, text_index, pat_index + 2)

    if pattern[pat_index] == '.' or text[text_index] == pattern[pat_index] or class_matching == True:
        return pattern_matching(text, pattern, text_index+1, pat_index+1)
    else:
        return False


print(pattern_matching("abc", "a.c"))
print(pattern_matching("abc", ".*"))
print(pattern_matching("aaabc", "a+b*c"))
print(pattern_matching("aaabc", "a+b*")) # should be false
print(pattern_matching("aaabc", "a+b*d?c?"))
print(pattern_matching("abc", ".*.*.*"))
print(pattern_matching("abc", ".*abc"))
print(pattern_matching("abc", ".*abcd")) #should be false
print(pattern_matching("abc", "[\w]+bc"))
print(pattern_matching("abc", "[\w]+bc"))
print(pattern_matching("d999auw", "[\w][\d]+auw*"))
print(pattern_matching("d999auw", "[\w][\d]+auw+.")) # should be false
print(pattern_matching("d999auw", "[\w][\d]+auw*."))
print((pattern_matching("aughasdkljf", ".*.*.*.*.*.*")))
print((pattern_matching("aughasdkljf", "a*b*c*f*.*.*")))
print((pattern_matching("aughasdkljf", "a*[\w]*")))
print((pattern_matching("aughasdkljf", "[\d]+*[\w]*"))) #should be false
print((pattern_matching("aughasdkljf", "[\d]*[\w]*")))