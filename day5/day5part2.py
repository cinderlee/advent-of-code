FILE_NM = 'day5input.txt'
ROW_CHARS_NUM = 7
NUM_ROWS = 128
NUM_COLS = 8

def get_row(binary_space_partition_line):
    start = 0
    end = start + NUM_ROWS - 1
    for index in range(ROW_CHARS_NUM):
        char = binary_space_partition_line[index]
        num_rows = end - start + 1
        half = num_rows // 2
        if char == 'F':
            end -= half
        else:
            start += half
    # start will equal end
    return start

def get_col(binary_space_partition_line):
    start = 0
    end = start + NUM_COLS - 1
    for index in range(ROW_CHARS_NUM, len(binary_space_partition_line)):
        char = binary_space_partition_line[index]
        num_cols = end - start + 1
        half = num_cols // 2
        if char == 'L':
            end -= half
        else:
            start += half
    return start

def get_seat_id(binary_space_partition_line):
    row = get_row(binary_space_partition_line)
    col = get_col(binary_space_partition_line)
    return row * 8 + col

def get_seat_ids(file_nm):
    file = open(file_nm)
    seat_ids = []

    for line in file:
        line = line.strip('\n')
        seat_ids.append(get_seat_id(line))
    
    file.close()
    return seat_ids

def get_missing_id(seat_ids_lst):
    min_id = min(seat_ids_lst)
    max_id = max(seat_ids_lst)
    for id in range(min_id, max_id):
        if id not in seat_ids_lst:
            return id

def solve(file_nm):
    seat_ids = get_seat_ids(file_nm)
    return get_missing_id(seat_ids)

def main():
    assert(get_seat_id('BFFFBBFRRR') == 567)
    assert(get_seat_id('FFFBBBFRRR') == 119)
    assert(get_seat_id('BBFFBBFRLL') == 820)
    assert(get_seat_id('FBFBBFFRLR') == 357)
    print(solve(FILE_NM))

main()
