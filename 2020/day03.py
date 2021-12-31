# Day 3: Toboggan Trajectory

INPUT_FILE_NAME = "./inputs/day03input.txt"
TEST_FILE_NAME = "./inputs/day03testinput.txt"

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def read_map_file(file_nm):
    '''
    Returns a two-dimensional array representing a map,
    where # represents a tree and . represents open squares.
    '''
    grid_map = []
    file = open(file_nm, 'r')

    for line in file:
        row = [elem for elem in line.strip('\n')]
        grid_map.append(row)

    file.close()
    return grid_map

def travel(grid_map, slope_x, slope_y):
    '''
    Returns the number of trees encountered following a slope.
    '''
    trees_encountered = 0
    curr_x = 0      # current col
    curr_y = 0      # current row

    while curr_y < len(grid_map):
        if grid_map[curr_y][curr_x] == '#':
            trees_encountered += 1
        curr_x = (curr_x + slope_x) % len(grid_map[0])
        curr_y += slope_y
    return trees_encountered

def solve_part_one(grid_map):
    '''
    Returns the number of trees encountered if the toboggan
    follows the slope of right 3 and down 1.
    '''
    return travel(grid_map, 3, 1)

def solve_part_two(grid_map):
    '''
    Returns the product of the number of trees encountered
    for each slope defined in SLOPES
    '''
    tree_product = 1
    for slope_x, slope_y in SLOPES:
        num_trees_encountered = travel(grid_map, slope_x, slope_y)
        tree_product *= num_trees_encountered
    return tree_product

def main():
    test_grid_map = read_map_file(TEST_FILE_NAME)
    assert(solve_part_one(test_grid_map) == 7)
    assert(solve_part_two(test_grid_map) == 336)

    grid_map = read_map_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(grid_map))
    print('Part Two:', solve_part_two(grid_map))

main()