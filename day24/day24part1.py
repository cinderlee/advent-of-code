dirs = {
    'e': (2, 0),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'se': (1, -1)
}

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

def count_black_tiles(tiles_dict):
    count_black = 0
    for elem in tiles_dict:
        if tiles_dict[elem]:
            count_black +=1

    return count_black


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

print(count_black_tiles(tiles))

    

    