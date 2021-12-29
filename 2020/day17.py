# Day 17: Conway Cybes

INPUT_FILE_NAME = "./inputs/day17input.txt"
TEST_FILE_NAME = "./inputs/day17testinput.txt"
NUM_CYCLES = 6

def read_file(file_nm):
    '''
    Returns a 2-dimensional list representation of the initial 
    state of Conway Cubes.
    '''
    file = open(file_nm, 'r')
    cubes = [list(row) for row in file.read().split('\n')]
    file.close()
    return cubes

def get_active_cubes(conway_cubes, pocket_dimension_size):
    '''
    Returns the set of active cubes in a pocket dimension given 
    the initial state. Each active cube is represented as a tuple
    with the correct number of coordinates. Start values of the 
    additional coordinates (z and w) are 0.

    For example, if an active cube is at (2, 1) in the initial state 
    and the pocket dimension size is 3, the active cube will be 
    represented as (2, 1, 0).
    '''
    active_cubes = set()
    for row in range(len(conway_cubes)):
        for col in range(len(conway_cubes[0])):
            cube = conway_cubes[row][col]
            if cube == '#':
                # start values of the remaining coordinates (z and w) are 0
                active_cubes.add(tuple([row, col] + [0 for i in range(pocket_dimension_size - 2)]))
    return active_cubes

def get_neighbors_3D(i, j, k):
    '''
    Returns a list of neighbor coordinates given a 
    current location (i, j, k).
    '''
    neighbor_lst = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            for z in range(k - 1, k + 2):
                if x == i and j == y and k == z:
                    continue
                neighbor_lst.append((x, y, z))
    return neighbor_lst

def get_neighbors_4D(i, j, k, l):
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

def simulate_cycles_3D(active_set, num_cycles):
    '''
    Returns the set of active cubes after performing simulating
    energy boot process.
    '''
    cycle_count = 0
    while cycle_count < num_cycles:
        neighbor_counts = {}
        for x, y, z in active_set:
            neighbor_lst = get_neighbors_3D(x, y, z)
            for neighbor in neighbor_lst:
                if neighbor in neighbor_counts:
                    neighbor_counts[neighbor] += 1
                else:
                    neighbor_counts[neighbor] = 1

        active_set = get_updated_active_set(neighbor_counts, active_set)
        cycle_count += 1
    return active_set

def simulate_cycles_4D(active_set, num_cycles):
    '''
    Returns the set of active cubes after performing simulating
    energy boot process.
    '''
    cycle_count = 0
    while cycle_count < num_cycles:
        neighbor_counts = {}
        for x, y, z, w in active_set:
            neighbor_lst = get_neighbors_4D(x, y, z, w)
            for neighbor in neighbor_lst:
                if neighbor in neighbor_counts:
                    neighbor_counts[neighbor] += 1
                else:
                    neighbor_counts[neighbor] = 1

        active_set = get_updated_active_set(neighbor_counts, active_set)
        cycle_count += 1
    return active_set

def solve_part_one(conway_cubes, num_cycles):
    '''
    Returns number of cubes left in active state after 
    performing simulations in a pocket dimension of size 3.
    '''
    active_cube_set = get_active_cubes(conway_cubes, 3)
    active_cube_set = simulate_cycles_3D(active_cube_set, num_cycles)
    return len(active_cube_set)

def solve_part_two(conway_cubes, num_cycles):
    '''
    Returns number of cubes left in active state after 
    performing simulations in a pocket dimension of size 4.
    '''
    active_cube_set = get_active_cubes(conway_cubes, 4)
    active_cube_set = simulate_cycles_4D(active_cube_set, num_cycles)
    return len(active_cube_set)

def main():
    test_conway_cubes = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_conway_cubes, NUM_CYCLES) == 112)
    assert(solve_part_two(test_conway_cubes, NUM_CYCLES) == 848)
    
    conway_cubes = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(conway_cubes, NUM_CYCLES))
    print('Part Two:', solve_part_two(conway_cubes, NUM_CYCLES))

main()
