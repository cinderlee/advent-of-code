FILE_NM = 'day5input.txt'
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
    Returns the seat id of a boarding pass, which is determined by 
    (row number * 8) + column number
    '''
    row = get_row(boarding_pass)
    col = get_col(boarding_pass)
    return row * 8 + col

def find_max_seating_id(file_nm):
    '''
    Returns the max seat id in file containing a list 
    of boarding passes
    '''
    file = open(file_nm)
    max_seat_id = 0

    for line in file:
        line = line.strip('\n')
        seat_id = get_seat_id(line)
        max_seat_id = max(max_seat_id, seat_id)

    file.close()
    return max_seat_id

def main():
    assert(get_seat_id('BFFFBBFRRR') == 567)
    assert(get_seat_id('FFFBBBFRRR') == 119)
    assert(get_seat_id('BBFFBBFRLL') == 820)
    assert(get_seat_id('FBFBBFFRLR') == 357)
    print(find_max_seating_id(FILE_NM))

main()