# Day 5: Binary Boarding

INPUT_FILE_NAME = "./inputs/day05input.txt"

ROW_CHARS_NUM = 7
NUM_ROWS = 128
NUM_COLS = 8

def get_row(boarding_pass):
    '''
    Returns the row number of a boarding pass, which uses
    binary space partitioning
    '''
    start = 0
    end = start + NUM_ROWS - 1
    for index in range(ROW_CHARS_NUM):
        char = boarding_pass[index]
        num_rows = end - start + 1
        half = num_rows // 2
        if char == 'F':
            end -= half
        else:
            start += half
    # start will equal end
    return start

def get_col(boarding_pass):
    '''
    Returns the col number of a boarding pass, which uses
    binary space partitioning
    '''
    start = 0
    end = start + NUM_COLS - 1
    for index in range(ROW_CHARS_NUM, len(boarding_pass)):
        char = boarding_pass[index]
        num_cols = end - start + 1
        half = num_cols // 2
        if char == 'L':
            end -= half
        else:
            start += half
    return start

def get_seat_id(boarding_pass):
    '''
    Returns the seat ID of a boarding pass, which uses
    binary space partitioning
    '''
    row = get_row(boarding_pass)
    col = get_col(boarding_pass)
    return row * 8 + col

def read_seat_ids(file_nm):
    '''
    Returns a list of seat ids from reading a file of
    boarding passes
    '''
    file = open(file_nm, 'r')
    seat_ids = []

    for line in file:
        line = line.strip('\n')
        seat_ids.append(get_seat_id(line))
    
    file.close()
    return seat_ids

def get_max_seating_id(seat_ids):
    '''
    Returns the max seat id in file containing a list 
    of boarding passes
    '''
    return max(seat_ids)

def get_missing_id(seat_ids):
    '''
    Returns the seat id of the missing boarding pass.
    The seat IDs +1 and -1 from the missing id exist in 
    the list of seat ids.
    '''
    min_id = min(seat_ids)
    max_id = max(seat_ids)
    for id in range(min_id, max_id):
        if id not in seat_ids:
            return id

def solve_part_one(seat_ids):
    return get_max_seating_id(seat_ids)

def solve_part_two(seat_ids):
    return get_missing_id(seat_ids)

def main():
    assert(get_seat_id('BFFFBBFRRR') == 567)
    assert(get_seat_id('FFFBBBFRRR') == 119)
    assert(get_seat_id('BBFFBBFRLL') == 820)
    assert(get_seat_id('FBFBBFFRLR') == 357)

    seat_ids = read_seat_ids(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(seat_ids))
    print('Part Two:', solve_part_two(seat_ids))

main()
