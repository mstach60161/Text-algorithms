import numpy as np
from unidecode import unidecode

MAX = 1000


def delta1(a, b):
    if a == b:
        return 0
    else:
        return 1


def delta2(a, b):
    if a == b:
        return 0
    elif unidecode(a) == unidecode(b):
        return 0.5
    else:
        return 1


def find_path(edit_table, x, y, path):
    if edit_table[x, y] == 0:
        return path

    if x-1 < 0:
        left, up, diag = edit_table[x, y-1], MAX, edit_table[x-1, y-1]
    elif y-1 < 0:
        left, up, diag = MAX, edit_table[x-1, y], edit_table[x - 1, y - 1]
    else:
        left, up, diag = edit_table[x, y-1], edit_table[x-1, y], edit_table[x - 1, y - 1]

    direction = min(left, up, diag)

    if direction == diag:
        if direction < edit_table[x, y]:
            path.append(('REP', [x-1, y-1]))
        return find_path(edit_table, x - 1, y - 1, path)
    elif direction == left:
        if direction < edit_table[x, y]:
            path.append(('ADD', [x, y-1]))
        return find_path(edit_table, x, y-1, path)
    else:
        if direction < edit_table[x, y]:
            path.append(('RM', [x-1, y]))
        return find_path(edit_table, x-1, y, path)


def visualisation(path, text1, text2):
    for operation, position in reversed(path):
        if operation == 'REP':
            print("Pozycja:", position[1]," Zamiana litery", text1[position[0]], "na litere", text2[position[1]])
        if operation == 'ADD':
            print("Pozycja:", position[1], "Dodanie litery", text2[position[0]])
        if operation == 'RM':
            print("Pozycja:", position[1], "Usuniecie litery", text1[position[1]])


def edit_distance(x, y, delta):
    edit_table = np.empty((len(x) + 1, len(y) + 1))
    for i in range(len(x) + 1):
        edit_table[i, 0] = i
    for j in range(len(y) + 1):
        edit_table[0, j] = j

    for i in range(len(x)):
        k = i + 1
        for j in range(len(y)):
            l = j + 1
            edit_table[k, l] = min(edit_table[k - 1, l] + 1,
                                   edit_table[k, l - 1] + 1,
                                   edit_table[k - 1, l - 1] + delta(x[i], y[j]))
    visualisation(find_path(edit_table, len(x), len(y), []), x, y)
    return edit_table[len(x), len(y)]


print("Ilosc operacji:",edit_distance('los', 'kloc', delta2), "\n")

print("Ilosc operacji:",edit_distance('Łódź', 'Lodz', delta2), "\n")

print("Ilosc operacji:",edit_distance('ATGAATCTTACCGCCTCG', 'ATGAGGCTCTGGCCCCTG', delta2), "\n")


