def get_neighbors(i, j, k):
    lst = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            for z in range(k - 1, k + 2):
                if x == i and j == y and k == z:
                    continue
                lst.append((x, y, z))

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

row = 0
for line in file:
    line = line.strip('\n')
    col = 0
    for elem in line:
        if elem == '#':
            # start value of z is 0
            valid.add((row, col, 0))
        col += 1
    row += 1
file.close()

max_cycles = 6
cycle_count = 0 

while cycle_count < max_cycles:
    neighbor_count = {}
    for x, y, z in valid:
        neighbor_lst = get_neighbors(x, y, z)
        for elem in neighbor_lst:
            if elem in neighbor_count:
                neighbor_count[elem] += 1
            else:
                neighbor_count[elem] = 1

    valid = get_new_valid_set(neighbor_count, valid)
    cycle_count += 1

print(len(valid))
