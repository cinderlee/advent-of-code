def get_neighbors(i, j, k, l):
    lst = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            for z in range(k - 1, k + 2):
                for w in range(l - 1, l + 2):
                    if x == i and j == y and k == z and l == w:
                        continue
                    lst.append((x, y, z, w))

    return lst

def get_new_valid_set(neighbor_counts, valid_set):
    new_valid_set = set()
    for elem in neighbor_counts:
        if elem in valid_set and (neighbor_counts[elem] == 2 or neighbor_counts[elem] == 3):
            new_valid_set.add(elem)
        elif elem not in valid_set and neighbor_counts[elem] == 3:
            new_valid_set.add(elem)

    return new_valid_set

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
            # start value of z and w
            valid.add((r, c, 0, 0))

max_cycles = 6
cycle_count = 0 

while cycle_count < max_cycles:
    neighbor_count = {}
    
    for x, y, z, w in valid:
        neighbor_lst = get_neighbors(x, y, z, w)
        for elem in neighbor_lst:
            if elem in neighbor_count:
                neighbor_count[elem] += 1
            else:
                neighbor_count[elem] = 1

    valid = get_new_valid_set(neighbor_count, valid)
    cycle_count += 1

print(len(valid))


