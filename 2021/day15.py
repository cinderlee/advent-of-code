import heapq

# Day 15: Chiton

INPUT_FILE_NAME = "./inputs/day15input.txt"
TEST_FILE_NAME = "./inputs/day15testinput.txt"

def parse_file(file_nm):
    '''
    Returns a 2D list representation of the map of the risk level
    of the chiton density in the cave. 
    '''
    file = open(file_nm, 'r')

    risk_map = []
    for line in file:
        line = line.strip('\n')
        risk_row = [int(risk) for risk in line]
        risk_map.append(risk_row)

    file.close()
    return risk_map

def generate_next_steps(risk_map, risk_total, row, col):
    '''
    Returns a list of the next possible states the submarine can be in 
    given the current location row, col. The submarine cannot move
    diagonally.

    Each state contains the minimum risk total at the current location
    and row and column of the next location.
    '''
    next_steps = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for row_disp, col_disp in directions:
        next_row = row + row_disp
        next_col = col + col_disp

        if next_row < 0 or next_row == len(risk_map) or next_col < 0 or next_col == len(risk_map[0]):
            continue
        next_steps.append((risk_total, next_row, next_col))
    return next_steps
        

def find_least_risk_path_total(risk_map):
    '''
    The submarine needs to exit a cave but the walls are covered in chitons.
    To avoid bumping into the chitons, the submarine needs to follow
    a path with the lowest risk, starting from top left and ending at the 
    bottom right of the map. 

    Returns the total of the path with the lowest risk. 
    '''
    seen_locations = set()
    # initial state has negative risk total since starting point's 
    # risk value is not included in the risk total
    risk_heap = [(-risk_map[0][0], 0, 0)]

    while len(risk_heap):
        risk_total, row, col = heapq.heappop(risk_heap)
        if row == len(risk_map) - 1 and col == len(risk_map[0]) - 1:
            return risk_total + risk_map[row][col]
        if (row, col) in seen_locations:
            continue
        seen_locations.add((row, col))
        
        risk_heap.extend(generate_next_steps(risk_map, risk_total + risk_map[row][col], row, col))
        heapq.heapify(risk_heap)

def generate_larger_cave_map(risk_map, enlarge_factor):
    '''
    Returns a x times larger map of the original risk map. The map tiles
    repeat to the right and downward but each time a tile repeats, its 
    risk increases by 1. A risk value above 9 wraps back to 1.
    '''
    larger_map = []
    for row in risk_map:
        larger_map_row = []
        for i in range(enlarge_factor):
            for risk in row:
                risk_elem = risk + i
                if risk_elem > 9:
                    risk_elem -= 9
                larger_map_row.append(risk_elem)
        larger_map.append(larger_map_row)

    original_length = len(larger_map)
    for i in range(1, enlarge_factor):
        for row in range(original_length):
            larger_map_row = []
            for risk in larger_map[row]:
                risk_elem = risk + i
                if risk_elem > 9:
                    risk_elem -= 9
                larger_map_row.append(risk_elem)
            larger_map.append(larger_map_row)
    return larger_map

def solve_part_one(risk_map):
    return find_least_risk_path_total(risk_map)

def solve_part_two(risk_map):
    larger_risk_map = generate_larger_cave_map(risk_map, 5)
    return find_least_risk_path_total(larger_risk_map)

def main():
    test_risk_map = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_risk_map) == 40)
    assert(solve_part_two(test_risk_map) == 315)

    risk_map = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(risk_map))
    print('Part Two:', solve_part_two(risk_map))

main()
