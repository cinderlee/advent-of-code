# Day 9: Smoke Basin

INPUT_FILE_NAME = "./inputs/day09input.txt"
TEST_FILE_NAME = "./inputs/day09testinput.txt"

def parse_file(file_nm):
    '''
    Returns the heightmap of the cave in the form of a 2D array.
    '''
    file = open(file_nm, 'r')
    heightmap = [[int(height) for height in row] for row in file.read().split('\n')]
    file.close()
    return heightmap

def get_adjacent_locations(heightmap, row, col):
    '''
    Returns a list of adjacent locations given the heightmap, current row,
    and current column. Diagonal locations are not considered.
    '''
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent_locations = []
    for dir_row, dir_col in directions:
        adjacent_row = row + dir_row
        adjacent_col = col + dir_col
        if adjacent_row >= 0 and adjacent_row < len(heightmap) and adjacent_col >= 0 and adjacent_col < len(heightmap[0]):
            adjacent_locations.append((adjacent_row, adjacent_col))
    return adjacent_locations

def get_low_points(heightmap):
    '''
    Returns a list of the lowest points in the cave given the heightmap.
    '''
    low_points = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            adjacent_locations = get_adjacent_locations(heightmap, row, col)
            is_lowest = True
            for loc_row, loc_col in adjacent_locations:
                if heightmap[loc_row][loc_col] <= heightmap[row][col]:
                    is_lowest = False
                    break

            if is_lowest:
                low_points.append((row, col))
    
    return low_points

def get_sum_risk_levels(heightmap, locations):
    '''
    Returns the sum of the risk levels given a list of locations
    in the heightmap. The risk level is 1 + the height.
    '''
    return sum([heightmap[row][col] for row, col in locations]) + len(locations)

def get_basin_size(heightmap, row, col):
    '''
    Return the basin size given the heightmap, current row, and current col. 
    Locations of height 9 are not included in the basin size. Every location
    is part of a basin.
    '''
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    size = 0
    locations = [(row, col)]
    seen = set()
    while locations:
        curr_row, curr_col = locations.pop()

        if curr_row < 0 or curr_row == len(heightmap) or curr_col < 0 or curr_col == len(heightmap[0]):
            continue
        if heightmap[curr_row][curr_col] == 9:
            continue
        if (curr_row, curr_col) in seen:
            continue
        
        size += 1
        seen.add((curr_row, curr_col))
        
        for dir_row, dir_col in directions:
            locations.append((curr_row + dir_row, curr_col + dir_col))

    return size

def get_basin_sizes(heightmap, lowest_points):
    '''
    Returns a list of basin sizes. A basin includes all locations that flow 
    down to a lowest point, meaning that each lowest point is in a separate basin. 
    Every location is part of one basin, except for locations of height 9.
    '''
    basin_sizes = [get_basin_size(heightmap, row, col) for row, col in lowest_points]
    return basin_sizes

def solve_part_one(heightmap):
    '''
    Returns the sum of the risk levels of the lowest points 
    in the cave. 
    '''
    cave_low_points = get_low_points(heightmap)
    return get_sum_risk_levels(heightmap, cave_low_points)

def solve_part_two(heightmap):
    '''
    Returns the product of the three largest basins in the cave.
    '''
    cave_low_points = get_low_points(heightmap)
    basin_sizes = get_basin_sizes(heightmap, cave_low_points)
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def main():
    test_heightmap = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_heightmap) == 15)
    assert(solve_part_two(test_heightmap) == 1134)

    heightmap = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(heightmap))
    print('Part Two:', solve_part_two(heightmap))

main()