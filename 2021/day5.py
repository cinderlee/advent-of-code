# Day 4: Giant Squid

INPUT_FILE_NAME = "./inputs/day5input.txt"
TEST_FILE_NAME = "./inputs/day5testinput.txt"

def parse_file(file_nm):
    line_coordinates = []
    file = open(file_nm, 'r')

    for line in file:
        start, end = line.strip('\n').split(' -> ')
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        line_coordinates.append([int(start_x), int(start_y), int(end_x), int(end_y)])

    file.close()
    return line_coordinates

def count_points(line_properties, points_count_map):
    points = None
    if 'x' in line_properties:
        x = line_properties['x']
        points = [(x, y) for y in line_properties['range']]
    elif 'y' in line_properties:
        y = line_properties['y']
        points = [(x, y) for x in line_properties['range']]
    else:
        x_range = line_properties['x-range']
        y_range = line_properties['y-range']

        points = zip(x_range, y_range)
    for point in points:
        if point in points_count_map:
            points_count_map[point] += 1
        else:
            points_count_map[point] = 1


def count_intersection_points(line_coordinates, should_count_diagonals):
    points_count_map = {}
    for coordinates in line_coordinates:
        start_x, start_y, end_x, end_y = coordinates
        
        if start_x == end_x:
            min_y = min(start_y, end_y)
            max_y = max(start_y, end_y)
            count_points({ 'x': start_x, 'range': range(min_y, max_y + 1 )}, points_count_map)

        elif start_y == end_y:
            min_x = min(start_x, end_x)
            max_x = max(start_x, end_x)
            count_points({ 'y': start_y, 'range': range(min_x, max_x + 1 )}, points_count_map)

        elif should_count_diagonals:
            x_disp, y_disp  = 1, 1

            if start_x > end_x:
                x_disp = -1

            if start_y > end_y:
                y_disp = -1

            x_range = range(start_x, end_x + x_disp, x_disp)
            y_range = range(start_y, end_y + y_disp, y_disp)
            
            count_points({ 
                'x-range': range(start_x, end_x + x_disp, x_disp), 
                'y-range': range(start_y, end_y + y_disp, y_disp)
            }, points_count_map)


    intersections = 0
    for count in points_count_map.values():
        if count > 1:
            intersections += 1
    return intersections

def solve_part_one(line_coordinates):
    '''
    Returns the score of the first winning board from calling a set of drawn
    numbers. The score is the product of the number that was drawn and 
    the sum of unmarked numbers on the winning board.
    '''
    return count_intersection_points(line_coordinates, False)
    

def solve_part_two(line_coordinates):
    '''
    Returns the score of the last winning board from calling a set of drawn
    numbers. The score is the product of the number that was drawn and 
    the sum of unmarked numbers on the winning board.
    '''
    return count_intersection_points(line_coordinates, True)

def main():
    test_line_coordinates = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_line_coordinates) == 5)
    assert(solve_part_two(test_line_coordinates) == 12)

    line_coordinates = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(line_coordinates))
    print('Part Two:', solve_part_two(line_coordinates))

main()
