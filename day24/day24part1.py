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

def count_black_tiles(tiles_dict):
    '''
    Returns the number of tiles with black side up
    '''
    count = 0
    for tile in tiles_dict:
        if tiles_dict[tile]:
            count +=1

    return count

def flip_tiles(file_nm):
    '''
    Flips hexagonal tiles from a file that contains a list of tiles 
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

def solve(file_nm):
    '''
    Returns the number of black tiles after flipping the tiles listed in a file.
    '''
    return count_black_tiles(flip_tiles(file_nm))

def main():
    assert(solve(FILE_TEST_NM) == 10)
    print(solve(FILE_NM))


main()

    

    