FILE_TEST_NM = 'day12testinput.txt'
FILE_NM = 'day12input.txt'
START_DIR = (1, 0)      # East

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

def rotate(curr_direction, turn, angle):
    '''
    Given a direction and angle, return the new 
    rotated direction
    '''
    x, y = curr_direction
    while angle > 0:
        if turn == 'R':
            x, y = y, -1 * x
        else:
            x, y = -1 * y, x
        angle -= 90
    return x, y

def move(navigation_instructions, start_dir):
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
            curr_dir = rotate(curr_dir, dir, disp)
            continue
        if dir == 'F' and -1 in curr_dir:
            disp = disp * -1
            
        horizontal = dir == 'E' or dir == 'W' or (
            dir == 'F' and (curr_dir == (1,0) or curr_dir == (-1, 0))
        )
        if horizontal:
            x += disp
        else:
            y += disp

    return x, y

def manhattan_distance(x, y):
    ''' 
    Returns manhattan distance given the horizontal and 
    vertical displacements
    '''
    return abs(x) + abs(y)

def solve(file_nm):
    nav_instr = read_file(file_nm)
    final_x, final_y = move(nav_instr, START_DIR)
    return manhattan_distance(final_x, final_y)

def main():
    assert(solve(FILE_TEST_NM) == 25)
    print(solve(FILE_NM))

main()