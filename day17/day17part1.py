file = open('day17input.txt')

valid = set()

lst = []
for line in file:
    line = line.strip('\n')
    sub_lst = []
    for elem in line:
        sub_lst.append(elem)

    lst.append(sub_lst)

file.close()


for r in range(len(lst)):
    for c in range(len(lst[0])):
        if lst[r][c] == '#':
            # start value of z
            valid.add((r, c, 0))

def get_neighbors(i, j, k):
    lst = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            for z in range(k - 1, k + 2):
                if x == i and j == y and k == z:
                    continue
                lst.append((x, y, z))

    return lst


max_cycles = 6
cycle_count = 0 

while cycle_count < 6:
    neighbor_count = {}
    for x, y, z in valid:
        neighbor_lst = get_neighbors(x, y, z)
        for elem in neighbor_lst:
            if elem in neighbor_count:
                neighbor_count[elem] += 1
            else:
                neighbor_count[elem] = 1

    new_valid_set = set()
    for elem in neighbor_count:
        if elem in valid and (neighbor_count[elem] == 2 or neighbor_count[elem] == 3):
            new_valid_set.add(elem)
        elif elem not in valid and neighbor_count[elem] == 3:
            new_valid_set.add(elem)

    valid = new_valid_set
    cycle_count += 1

print(len(valid))


