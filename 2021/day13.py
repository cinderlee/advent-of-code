# Day 13: Transparent Origami

INPUT_FILE_NAME = "./inputs/day13input.txt"
TEST_FILE_NAME = "./inputs/day13testinput.txt"

def parse_coordinate(line):
    '''
    Returns a tuple representing the location of a dot on the 
    transparent paper read from a file line.
    '''
    col, row = line.split(',')
    return int(col), int(row)

def parse_fold_instruction(line):
    '''
    Returns a tuple representing the fold instruction read from a file line.
    If the line specified is a horizontal line, the instruction will
    be to fold the paper up. Otherwise, it will be fold the paper to the left.
    '''
    line_def = line.split(' ')[-1]
    direction, num = line_def.split('=')
    if (direction == 'y'):
        return 'up', int(num)
    else:
        return 'left', int(num)

def parse_file(file_nm):
    '''
    Returns a map of coordinates of the transparent paper where the 
    dots are located, a list of fold instructions, the number of rows,
    and the number of columns of the coordinate grid.
    '''
    num_rows = 0
    num_cols = 0
    fold_instructions = []
    coords = dict()
    is_fold_instruction = False

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')

        if line == '':
            is_fold_instruction = True
            continue

        if not is_fold_instruction:
            col, row = parse_coordinate(line)
            coords[(row, col)] = '#'
            num_rows = max(num_rows, row)
            num_cols = max(num_cols, col)
        else:
            fold_instructions.append(parse_fold_instruction(line))

    file.close()
    return coords, fold_instructions, num_rows + 1, num_cols + 1

def fold_up(coords, num_cols, row_num):
    '''
    Folds the transparent paper up on a row given the row number. The
    bottom half of the paper is folded up and if dots overlap, they become
    a single dot.
    '''
    for i in range(row_num + 1): 
        for j in range(num_cols):
            top = '.'
            bot = '.'
            if (row_num - i, j) in coords:
                top = coords[(row_num - i, j)]
            if (row_num + i, j) in coords:
                bot = coords[(row_num + i, j)]
            if top == '#' or bot == '#':
                coords[(row_num - i, j)] = '#'
            else:
                coords[(row_num - i, j)] = '.'

def fold_left(coords, num_rows, col_num):
    '''
    Folds the transparent paper left on a column given the column number. The
    right half of the paper is folded left and if dots overlap, they become
    a single dot.
    '''
    for i in range(num_rows):
        for j in range(col_num + 1):
            left = '.'
            right = '.'
            if (i, col_num - j) in coords:
                left = coords[(i, col_num - j)]
            if (i, col_num + j) in coords:
                right = coords[(i, col_num + j)]
            if left == '#' or right == '#':
                coords[(i, col_num - j)] = '#'
            else:
                coords[(i, col_num - j)] = '.'

def fold_paper(coords, fold_instructions, num_rows, num_cols, only_first_fold = False):
    '''
    Returns the final dimensions of the transparent paper after performing
    a set of fold instructions. 

    For part one, only the first fold is performed.
    '''
    for instruction in fold_instructions:
        direction, num = instruction

        if direction == 'up':
            fold_up(coords, num_cols, num)
            num_rows = num
        else: 
            fold_left(coords, num_rows, num)
            num_cols = num

        if only_first_fold:
            break
    return num_rows, num_cols

def solve_part_one(coords, fold_instructions, num_rows, num_cols):
    '''
    Returns the number of dots visible after the first fold instruction.
    '''
    num_rows, num_cols = fold_paper(coords, fold_instructions, num_rows, num_cols, True)
    dots_counter = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if (i, j) in coords and coords[(i, j)] == '#':
                dots_counter += 1
    return dots_counter

def solve_part_two(coords, fold_instructions, num_rows, num_cols):
    '''
    Displays the code to activate the infrared thermal imaging camera system
    after perform the set of the fold instructions on the transparent paper.
    '''
    num_rows, num_cols = fold_paper(coords, fold_instructions, num_rows, num_cols)
    for i in range(num_rows):
        for j in range(num_cols):
            if (i, j) in coords and coords[(i, j)] == '#':
                print('#', end = '')
            else:
                print('_', end = '')
        print()

def main():
    test_coords, test_fold_instructions, test_num_rows, test_num_cols = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_coords, test_fold_instructions, test_num_rows, test_num_cols) == 17)
    
    coords, fold_instructions, num_rows, num_cols = parse_file(INPUT_FILE_NAME)
    coords_copy = coords.copy()
    print("Part One:", solve_part_one(coords, fold_instructions, num_rows, num_cols))
    print("Part Two:")
    solve_part_two(coords_copy, fold_instructions, num_rows, num_cols)

main()