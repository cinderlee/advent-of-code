FILE_TEST_NM = 'day12testinput.txt'
FILE_NM = 'day12input.txt'

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

def rotate(waypt_x, waypt_y, turn, angle):
    '''
    Return the new location of waypoint after rotation.
    '''
    while angle > 0:
        if turn == 'R':
            waypt_x, waypt_y = waypt_y, -1 * waypt_x
        else:
            waypt_x, waypt_y = -1 * waypt_y, waypt_x
        angle -= 90
    return waypt_x, waypt_y

def move(navigation_instructions):
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


def solve(file_nm):
    nav_instr = read_file(file_nm)
    final_x, final_y = move(nav_instr)
    return manhattan_distance(final_x, final_y)

def main():
    assert(solve(FILE_TEST_NM) == 286)
    print(solve(FILE_NM))

main()