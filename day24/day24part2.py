dirs = {
    'e': (2, 0),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'se': (1, -1)
}

directions = list(dirs.values())

def get_loc(input_line):
    index = 0
    x = 0
    y = 0
    while index < len(input_line):
        if input_line[index] == 'e' or input_line[index] == 'w':
            dir_x, dir_y = dirs[input_line[index]]
            x, y = x + dir_x, y + dir_y
            index += 1

        else:
            dir_x, dir_y = dirs[input_line[index : index + 2]]
            x, y = x + dir_x, y + dir_y
            index += 2

    return x, y

def add_neighbors(tiles_dict):
    neighbors = set()

    for tile in tiles_dict:
        if not tiles_dict[tile]:
            continue
        x, y = tile

        for dir_x, dir_y in directions:
            neighbor_x = x + dir_x
            neighbor_y = y + dir_y

            neighbors.add((neighbor_x, neighbor_y))

    for neighbor in neighbors:
        if neighbor not in tiles_dict:
            tiles_dict[neighbor] = False

def count_black_neighbors(tiles_dict, loc):
    x, y = loc
    blacks = 0

    for dir_x, dir_y in directions:
        neighbor_x = x + dir_x
        neighbor_y = y + dir_y

        if (neighbor_x, neighbor_y) in tiles_dict:
            if tiles_dict[(neighbor_x, neighbor_y)]:
                blacks += 1 
    return blacks

def count_black_tiles(tiles_dict):
    count_black = 0

    for elem in tiles_dict:
        if tiles_dict[elem]:
            count_black +=1

    return count_black

def flip(tiles_dict):
    changes = []
    add_neighbors(tiles_dict)

    for elem in tiles_dict:
        black_neighbors = count_black_neighbors(tiles_dict, elem)

        if tiles_dict[elem] and (black_neighbors == 0 or black_neighbors > 2):
            changes.append((elem, False))

        elif not tiles_dict[elem] and black_neighbors == 2:
            changes.append((elem, True))

    for tile, val in changes:
        tiles_dict[tile] = val


file = open('day24input.txt')

tiles = {} 

for line in file:
    line = line.strip('\n')
    loc = get_loc(line)

    if loc in tiles:
        tiles[loc] = not tiles[loc]
    else:
        tiles[loc] = True

file.close()


day = 0 
while day < 100:
    flip(tiles)
    day += 1

print(count_black_tiles(tiles))
