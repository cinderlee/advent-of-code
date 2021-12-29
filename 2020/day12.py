# Day 12: Rain Risk

INPUT_FILE_NAME = "./inputs/day12input.txt"
TEST_FILE_NAME = "./inputs/day12testinput.txt"

def read_file(file_nm):
    '''
    Returns a list of navigation instructions from a file.
    An instruction is a tuple in the form of (action, value)
    '''
    file = open(file_nm, 'r')
    navigation_instr = []

    for line in file:
        line = line.strip('\n')
        if line[0] == 'S' or line[0] == 'W':
            navigation_instr.append((line[0], int(line[1:]) * -1))
        else:
            navigation_instr.append((line[0], int(line[1:])))

    file.close()
    return navigation_instr

def rotate(x, y, turn, angle):
    '''
    Rotate x and y given the direction and angle. x and y
    can represent the direction (part one) or location (of 
    waypoint in part two).
    '''
    while angle > 0:
        if turn == 'R':
            x, y = y, -1 * x
        else:
            x, y = -1 * y, x
        angle -= 90
    return x, y

def move_part_one(navigation_instructions, start_dir):
    '''
    Returns the accumulated displacements for x and y 
    after performing the navigation instructions

    Actions
        N: move north by given value
        S: move south by given value
        E: move east by given value
        W: move west by given value
        L: turn left by given number of degrees
        R: turn right by given number of degrees
        F: move forward by given value in direction ship is currently facing
    '''
    curr_dir = start_dir
    x = 0
    y = 0
    
    for dir, disp in navigation_instructions:
        if dir == 'R' or dir == 'L':
            curr_dir = rotate(curr_dir[0], curr_dir[1], dir, disp)
            continue
        if dir == 'F' and -1 in curr_dir:
            disp = disp * -1
            
        horizontal = dir == 'E' or dir == 'W' or (
            dir == 'F' and (curr_dir == (1, 0) or curr_dir == (-1, 0))
        )
        if horizontal:
            x += disp
        else:
            y += disp

    return x, y

def move_part_two(navigation_instructions):
    '''
    Returns the accumulated ship displacements for x and y 
    after performing the navigation instructions

    Waypoint starts 10 units east and 1 unit north relative to ship.

    Actions
        N: move waypoint north by given value
        S: move waypoint south by given value
        E: move waypoint east by given value
        W: move waypoint west by given value
        L: rotate waypoint around ship counterclockwise by given number of degrees
        R: rotate waypoint around ship clockwise by given number of degrees
        F: move ship forward to the waypoint a number of times equal to give value
    '''
    waypoint_x = 10
    waypoint_y = 1
    ship_x = 0
    ship_y = 0

    for dir, val in navigation_instructions:
        if dir == 'F':
            ship_x += val * waypoint_x
            ship_y += val * waypoint_y
        elif dir == 'R' or dir == 'L':
            waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, dir, val)
        else:
            if dir == 'E' or dir == 'W':
                waypoint_x += val
            else:
                waypoint_y += val

    return ship_x, ship_y

def manhattan_distance(x, y):
    ''' 
    Returns manhattan distance given the horizontal and 
    vertical displacements
    '''
    return abs(x) + abs(y)

def solve_part_one(navigation_instructions):
    start_dir = (1, 0)      # East
    final_x, final_y = move_part_one(navigation_instructions, start_dir)
    return manhattan_distance(final_x, final_y)

def solve_part_two(navigation_instructions):
    final_x, final_y = move_part_two(navigation_instructions)
    return manhattan_distance(final_x, final_y)

def main():
    test_navigation_instructions = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_navigation_instructions) == 25)
    assert(solve_part_two(test_navigation_instructions) == 286)

    navigation_instructions = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(navigation_instructions))
    print('Part Two:', solve_part_two(navigation_instructions))

main()