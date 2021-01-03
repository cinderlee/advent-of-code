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

def find_max_seating_id(file_nm):
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