import string

from aho_corasick import ahc_create_statemachine, ahc_find

file = open("haystack.txt", mode='r', encoding='utf-8')
text = file.read()
file.close()
lines = text.splitlines()

max_l = 0

for line in lines:
    if len(line) > max_l:
        max_l = len(line)

text_lines = []

for line in lines:
    text_lines.append(line.ljust(max_l, '#'))






#ZADANIE 2
print('ZADANIE 2')
patterns = list(string.ascii_lowercase)
root = ahc_create_statemachine(patterns)
old_dictionary = ahc_find(text_lines[0], root, patterns)

number = 0

for i in range(1, len(text_lines)):
    current_dictionary = ahc_find(text_lines[i], root, patterns)
    printed = False
    for letter in list(string.ascii_lowercase):
        similarities = set(old_dictionary[letter]) & set(current_dictionary[letter])
        if len(similarities) > 0:
            number += len(similarities)
            if printed is False:
                print("LINES", i - 1, "-", i)
                printed = True
            print(letter, "on position", similarities)
    old_dictionary = current_dictionary

print(number)

#ZADANIE 3
print('ZADANIE 3')
patterns = ['th', 't h']
root = ahc_create_statemachine(patterns)
old_dictionary = ahc_find(text_lines[0], root, patterns)
for i in range(1, len(text_lines)):
    current_dictionary = ahc_find(text_lines[i], root, patterns)

    for letter in list(patterns):
        similarities = set(old_dictionary[letter]) & set(current_dictionary[letter])
        if len(similarities) > 0:
            print("LINES", i - 1, "-", i)
            print(letter, "on position", similarities)
    old_dictionary = current_dictionary