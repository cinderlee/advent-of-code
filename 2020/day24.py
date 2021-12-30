# Day 24: Lobby Layout

INPUT_FILE_NAME = "./inputs/day24input.txt"
TEST_FILE_NAME = "./inputs/day24testinput.txt"

NUM_DAYS = 100

DIRS = {
    'e': (2, 0),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'se': (1, -1)
}

def read_file(file_nm):
    '''
    Returns a list of tiles read from a file.
    '''
    file = open(file_nm, 'r')
    tiles = file.read().split('\n')
    file.close()
    return tiles

def get_loc(input_line):
    '''
    A hexagonal tile has 6 neighbors: east, southeast, southwest, west, 
    northwest, and northeast, which are denoted by e, se, sw, w, nw, 
    and ne respectively. The tiles are placed in a hex grid. The input
    line represents a series of steps starting from a reference tile 
    in the center of the room. 

    Returns the location of the tile.
    '''
    index = 0
    x = 0
    y = 0
    while index < len(input_line):
        if input_line[index] == 'e' or input_line[index] == 'w':
            dir_x, dir_y = DIRS[input_line[index]]
            x, y = x + dir_x, y + dir_y
            index += 1
        else:
            dir_x, dir_y = DIRS[input_line[index : index + 2]]
            x, y = x + dir_x, y + dir_y
            index += 2

    return x, y

def set_up_tiles(tiles_lst):
    '''
    Sets up the floor of hexagonal tiles from a list of tiles that need 
    to be flipped over. All tiles are initially facing white side up.

    Returns a dictionary of tiles where the key is the tile location
    and the value determines whether the tile is black side up.
    '''
    tiles = {}
    for tile_directions in tiles_lst:
        loc = get_loc(tile_directions)

        if loc in tiles:
            tiles[loc] = not tiles[loc]
        else:
            tiles[loc] = True

    return tiles

def add_neighbors(tiles_dict):
    '''
    Adds tile locations adjacent to black tiles to a tile dictionary.
    '''
    neighbors = set()

    for tile in tiles_dict:
        if not tiles_dict[tile]:
            continue
        x, y = tile

        for dir_x, dir_y in DIRS.values():
            neighbor_x = x + dir_x
            neighbor_y = y + dir_y

            neighbors.add((neighbor_x, neighbor_y))

    for neighbor in neighbors:
        if neighbor not in tiles_dict:
            tiles_dict[neighbor] = False

def count_black_neighbors(tiles_dict, loc):
    '''
    Given a dictionary of tiles and a tile location, returns the number
    of blakc tiles adjacent to the location.
    '''
    x, y = loc
    count = 0

    for dir_x, dir_y in DIRS.values():
        neighbor_x = x + dir_x
        neighbor_y = y + dir_y

        if (neighbor_x, neighbor_y) in tiles_dict:
            if tiles_dict[(neighbor_x, neighbor_y)]:
                count += 1 
    return count

def count_black_tiles(tiles_dict):
    '''
    Returns the number of tiles with black side up
    '''
    count = 0
    for tile in tiles_dict:
        if tiles_dict[tile]:
            count +=1

    return count

def flip(tiles_dict):
    '''
    Each day, the tiles are flipped according to these rules:
        A black tile with 0 or more than 2 black tiles adjacent to it is flipped to white.
        A white tile with exactly 2 black tiles adjacent to it is flipped to black
    '''
    changes = []
    add_neighbors(tiles_dict)

    for elem in tiles_dict:
        black_neighbors = count_black_neighbors(tiles_dict, elem)

        if tiles_dict[elem] and (black_neighbors == 0 or black_neighbors > 2):
            changes.append((elem))

        elif not tiles_dict[elem] and black_neighbors == 2:
            changes.append((elem))

    for tile in changes:
        tiles_dict[tile] = not tiles_dict[tile]

def solve_part_one(tiles_lst):
    '''
    Returns the number of black tiles after flipping the tiles in the list.
    '''
    return count_black_tiles(set_up_tiles(tiles_lst))

def solve_part_two(tiles_lst, num_days):
    '''
    Returns the number of black tiles after flipping a floor of tiles for 
    a number of days.
    '''
    tiles = set_up_tiles(tiles_lst)

    day = 0 
    while day < num_days:
        flip(tiles)
        day += 1

    return count_black_tiles(tiles)

def main():
    test_tiles_lst = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_tiles_lst) == 10)
    assert(solve_part_two(test_tiles_lst, NUM_DAYS) == 2208)

    tiles_lst = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(tiles_lst))
    print('Part Two:', solve_part_two(tiles_lst, NUM_DAYS))

main()