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

def check_adjacent(x, y, lst):
    count = 0
    for row in range (x - 1, x + 2):
        for col in range (y - 1, y + 2):
            if row == x and col == y:
                continue
            if row < 0 or row >= len(lst) or col < 0 or col >= len(lst[0]):
                continue
            if lst[row][col] == '#':
                count += 1
    return count


changes = True
while changes:
    flips = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == '#' and check_adjacent(i, j, lst) >= 4:
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