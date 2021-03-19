from bisect import bisect
import random


def tokenize_with_lines(text):
    lines = []
    for line in text:
        if line != "\n":
            lines.append(line[:len(line) - 1])
    splitted_lines = []
    for line in lines:
        splitted_lines.append(line.split())
    return splitted_lines


def tokenize(text):
    splitted_lines = tokenize_with_lines(text)
    words = []
    for line in splitted_lines:
        for word in line:
            words.append(word)
    return words


def remove_from_tokens(tokens, number):
    for i in range(number):
        index = random.randint(0, len(tokens) - 1)
        tokens.pop(index)


def lcs(x, y):
    ranges = []
    ranges.append(len(y))
    y_letters = list(y)
    for i in range(len(x)):
        positions = [j for j, l in enumerate(y_letters) if l == x[i]]
        positions.reverse()
        for p in positions:
            k = bisect(ranges, p)
            if k == bisect(ranges, p):
                if k < len(ranges) - 1:
                    ranges[k] = p
                else:
                    ranges[k:k] = [p]
    return len(ranges) - 1


text = open("romeo-i-julia-700.txt", 'r')
tokens = tokenize(text)
tokens2 = tokens[:]

remove_from_tokens(tokens, int(len(tokens) * 0.03))
remove_from_tokens(tokens2, int(len(tokens2) * 0.03))

print(lcs(tokens, tokens2))

text.close()
