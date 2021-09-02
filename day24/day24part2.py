NUM_DAYS = 100
FILE_TEST_NM = 'day24testinput.txt'
FILE_NM = 'day24input.txt'

DIRS = {
    'e': (2, 0),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'se': (1, -1)
}

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

def set_up_tiles(file_nm):
    '''
    Sets up the floor of hexagonal tiles from a file that contains a list of tiles 
    that need to be flipped over. All tiles are initially facing white side up.

    Returns a dictionary of tiles where the key is the tile location
    and the value determines whether the tile is black side up.
    '''
    tiles = {}
    tiles_file = open(file_nm, 'r')
    for line in tiles_file:
        loc = get_loc(line.strip('\n'))

        if loc in tiles:
            tiles[loc] = not tiles[loc]
        else:
            tiles[loc] = True

    tiles_file.close()
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

def solve(file_nm, num_days):
    '''
    Returns the number of black tiles after flipping a floor of tiles for 
    a number of days.
    '''
    tiles = set_up_tiles(file_nm)

    day = 0 
    while day < num_days:
        flip(tiles)
        day += 1

    return count_black_tiles(tiles)

def main():
    assert(solve(FILE_TEST_NM, NUM_DAYS) == 2208)
    print(solve(FILE_NM, NUM_DAYS))


main()