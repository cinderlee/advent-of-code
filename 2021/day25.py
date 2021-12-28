# Day 25: Sea Cucumber

INPUT_FILE_NAME = "./inputs/day25input.txt"
TEST_FILE_NAME = "./inputs/day25testinput.txt"

def parse_file(file_nm):
    '''
    Returns a 2D list representing the seafloor of sea cucumbers, where
    > represents sea cucumbers that move east and v represents sea cucumbers
    that move south.
    '''
    sea_floor = []

    file = open(file_nm)
    for line in file:
        sea_floor.append(list(line.strip('\n')))
    file.close()

    return sea_floor

def move_east_herd(sea_floor):
    '''
    Moves the east herd of sea cucumbers on the sea floor. Returns true 
    if there is movement.

    All sea cucumbers simultaneously consider if they can move before proceeding
    and those that move past the right border wrap around to the left. 
    '''
    sea_cucumbers_to_move = []
    num_rows = len(sea_floor)
    num_cols = len(sea_floor[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if sea_floor[i][j] == '>' and sea_floor[i][(j + 1) % num_cols] == '.':
                sea_cucumbers_to_move.append((i, j))

    for loc in sea_cucumbers_to_move:
        i, j = loc 
        adjacent_j = (j + 1) % num_cols
        sea_floor[i][j], sea_floor[i][adjacent_j] = sea_floor[i][adjacent_j], sea_floor[i][j]

    return len(sea_cucumbers_to_move) > 0

def move_south_herd(sea_floor):
    '''
    Moves the south herd of sea cucumbers on the sea floor. Returns true 
    if there is movement.

    All sea cucumbers simultaneously consider if they can move before proceeding
    and those that move past the south border wrap around to the top. 
    '''
    sea_cucumbers_to_move = []
    num_rows = len(sea_floor)
    num_cols = len(sea_floor[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if sea_floor[i][j] == 'v' and sea_floor[(i + 1) % num_rows][j] == '.':
                sea_cucumbers_to_move.append((i, j))

    for loc in sea_cucumbers_to_move:
        i, j = loc 
        adjacent_i = (i + 1) % num_rows
        sea_floor[i][j], sea_floor[adjacent_i][j] = sea_floor[adjacent_i][j], sea_floor[i][j]
    
    return len(sea_cucumbers_to_move) > 0

def simulate_sea_cucumber_movement(sea_floor):
    '''
    Returns the number of steps for the sea cucumbers to finish moving. 
    At each step, the east herd (>) moves first and then the south herd.
    '''
    steps = 0
    is_not_done = True
    while is_not_done:
        has_east_movement = move_east_herd(sea_floor)
        has_south_movement = move_south_herd(sea_floor)
        steps += 1

        is_not_done = has_east_movement or has_south_movement
    return steps

def solve_part_one(sea_floor):
    '''
    Returns the number of steps it takes for sea cucumbers to finsih
    moving on the so that you can land the submarine.
    '''
    return simulate_sea_cucumber_movement(sea_floor)


def main():
    test_sea_floor = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_sea_floor) == 58)

    sea_floor = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(sea_floor))

main()
