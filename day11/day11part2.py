file = open('day11input.txt')
# file = open('day11testinput.txt')

lst = []
for line in file:
    sub = []
    line = line.strip('\n')
    for elem in line:
        if elem == 'L':
            sub.append('#')
        else:
            sub.append(elem)
    lst.append(sub)

file.close()


def check_adj_helper(x, y, dir_x, dir_y, lst):
    while x >= 0 and x < len(lst) and y >= 0 and y < len(lst[0]):
        if lst[x][y] == '.':
            x += dir_x
            y += dir_y
        elif lst[x][y] == '#':
            return True
        else:
            return False

def check_adjacent(x, y, lst):
    count = 0
    pos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dir_x, dir_y in pos:
        if check_adj_helper(x + dir_x, y + dir_y, dir_x, dir_y, lst):
            count += 1
    return count


changes = True
while changes:
    flips = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#' and check_adjacent(i, j, lst) >= 5:
                flips.append((i, j))
            elif lst[i][j] == 'L' and check_adjacent(i, j, lst) == 0:
                flips.append((i, j))
    changes = len(flips) > 0
    for r, c in flips:
        if lst[r][c] == '#':
            lst[r][c] = 'L'
        else:
            lst[r][c] = '#'

total = 0

for elem in lst:
    for elem2 in elem:
        if elem2 == '#':
            total += 1

print(total)