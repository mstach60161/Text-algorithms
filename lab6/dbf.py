import math
import sys
import objsize


def sort_rename(sequence):
    last_entry = None
    index = 0
    position_to_index = [None] * len(sequence)
    first_entry = {}
    for entry in sorted([(e, i) for i, e in enumerate(sequence)]):
        if last_entry and last_entry[0] != entry[0]:
            index += 1
            first_entry[index] = entry[1]

        position_to_index[entry[1]] = index
        if last_entry is None:
            first_entry[0] = entry[1]
        last_entry = entry
    return position_to_index, first_entry


def kmr(text):
    original_length = len(text)
    factor = math.floor(math.log2(len(text)))
    max_length = 2 ** factor
    padding_length = 2 ** (factor + 1) - 1
    text += "|" * padding_length

    position_to_index, first_entry = sort_rename(list(text))
    names = {1: position_to_index}
    entries = {1: first_entry}
    for i in range(1, factor):
        power = 2 ** (i - 1)
        new_sequence = []
        for j in range(len(text)):
            if j + power < len(names[power]):
                new_sequence.append((names[power][j], names[power][j + power]))
        position_to_index, first_entry = sort_rename(new_sequence)
        names[power * 2] = position_to_index
        entries[power * 2] = first_entry
    return names, entries


def find_dbf_old(text, pattern, names, entries):  # pierwsza wersja, tylko potegi 2
    length = len(pattern)
    positions = names[length]
    entry = entries[length]

    index = -1
    for i in range(len(entry)):
        if text[entry[i]:entry[i] + length] == pattern:
            index = i
            break
    if index == -1:
        return -1
    results = []
    for i in range(len(positions)):
        if positions[i] == index:
            results.append(i)
    return len(results)


def find_dbf(text, pattern, names, entries):
    factor = math.floor(math.log2(len(pattern)))
    suffix_len = 2 ** factor
    pattern_len = len(pattern)
    positions = names[suffix_len]
    entry = entries[suffix_len]

    left = -1
    for i in range(len(entry)):
        if text[entry[i]:entry[i] + suffix_len] == pattern[0:suffix_len]:
            left = i
            break

    right = -1
    for i in range(len(entry)):
        if text[entry[i]:entry[i] + suffix_len] == pattern[pattern_len - suffix_len:]:
            right = i
            break

    if left == -1 or right == -1:
        return -1

    results = []
    for i in range(len(positions)):
        if positions[i] == left and positions[i + pattern_len - suffix_len] == right:
            results.append(i)
    return len(results)


