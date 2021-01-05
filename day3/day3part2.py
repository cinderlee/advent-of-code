FILE_TEST_NM = 'day3testinput.txt'
FILE_NM = 'day3input.txt'
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

def read_map_file(file_nm):
    grid_map = []
    file = open(file_nm, 'r')

    for line in file:
        row = []
        for elem in line.strip('\n'):
            row.append(elem)
        grid_map.append(row)

    file.close()
    return grid_map

def travel(grid_map, slope_x, slope_y):
    trees_encountered = 0
    curr_x = 0      # current col
    curr_y = 0      # current row

    while curr_y < len(grid_map):
        if grid_map[curr_y][curr_x] == '#':
            trees_encountered += 1
        curr_x = (curr_x + slope_x) % len(grid_map[0])
        curr_y += slope_y
    return trees_encountered

def solve(file_nm):
    tree_product = 1
    grid_map = read_map_file(file_nm)
    for slope_x, slope_y in SLOPES:
        num_trees_encountered = travel(grid_map, slope_x, slope_y)
        tree_product *= num_trees_encountered
    return tree_product

def main():
    assert(solve(FILE_TEST_NM) == 336)
    print(solve(FILE_NM))

main()
