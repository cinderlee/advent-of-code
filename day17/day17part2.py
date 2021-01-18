FILE_TEST_NM = 'day17testinput.txt'
FILE_NM = 'day17input.txt'
NUM_CYCLES = 6

def read_file(file_nm):
    '''
    Reads initial state of Conway Cubes in pocket dimension. 
    The pocket dimension is an infinite 4-dimensional grid.
    Initial state represents 2-dimensional slice of grid.

    Returns a set of locations of the active hypercubes.
    '''
    active_hypercubes = set()
    file = open(file_nm, 'r')
    row = 0
    for line in file:
        line = line.strip('\n')
        col = 0
        for elem in line:
            if elem == '#':
               # start value of z and w is 0
                active_hypercubes.add((row, col, 0, 0,))
            col += 1
        row += 1
    file.close()
    return active_hypercubes

def get_neighbors(i, j, k, l):
    '''
    Returns a list of neighbor coordinates given a 
    current location (i, j, k, l).
    '''
    neighbor_lst = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            for z in range(k - 1, k + 2):
                for w in range(l - 1, l + 2):
                    if x == i and j == y and k == z and l == w:
                        continue
                    neighbor_lst.append((x, y, z, w))

    return neighbor_lst

def get_updated_active_set(neighbor_counts, curr_active_set):
    '''
    Returns a new set of active cubes. The current active set
    and dictionary where the location key is mapped to number of 
    active neighbors are given.
    '''
    new_active_set = set()
    for elem in neighbor_counts:
        if elem in curr_active_set and (neighbor_counts[elem] == 2 or neighbor_counts[elem] == 3):
            new_active_set.add(elem)
        elif elem not in curr_active_set and neighbor_counts[elem] == 3:
            new_active_set.add(elem)
    return new_active_set

def simulate_cycles(active_set, num_cycles):
    '''
    Returns the set of active cubes after performing simulating
    energy boot process.
    '''
    cycle_count = 0
    while cycle_count < num_cycles:
        neighbor_counts = {}
        for x, y, z, w in active_set:
            neighbor_lst = get_neighbors(x, y, z, w)
            for neighbor in neighbor_lst:
                if neighbor in neighbor_counts:
                    neighbor_counts[neighbor] += 1
                else:
                    neighbor_counts[neighbor] = 1

        active_set = get_updated_active_set(neighbor_counts, active_set)
        cycle_count += 1
    return active_set

def solve(file_nm, num_cycles):
    '''
    Returns number of cubes left in active state after 
    performing simulations.
    '''
    active_cube_set = read_file(file_nm)
    active_cube_set = simulate_cycles(active_cube_set, num_cycles)
    return len(active_cube_set)

def main():
    assert(solve(FILE_TEST_NM, NUM_CYCLES) == 848)
    print(solve(FILE_NM, NUM_CYCLES))

main()
