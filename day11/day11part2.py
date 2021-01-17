FILE_TEST_NM = 'day11testinput.txt'
FILE_NM = 'day11input.txt'
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def is_valid(row, col, lst):
    '''
    Returns whether row and col are valid indices.
    '''
    return row >= 0 and row < len(lst) and col >= 0 and col < len(lst[0])

def count_occupied_one_dir(row, col, dir_r, dir_c, grid):
    '''
    Returns whether a seat is occupied in a direction from
    current seat.
    '''
    while is_valid(row, col, grid):
        if grid[row][col] == '.':
            row += dir_r
            col += dir_c
        elif grid[row][col] == '#':
            return True
        else:
            return False
    
    return False

def count_occupied_eight_dirs(row, col, grid):
    '''
    Returns number of seats occupied in all 8 directions.
    '''
    count = 0
    for dir_r, dir_c in DIRECTIONS:
        start_row = row + dir_r
        start_col = col + dir_c
        if count_occupied_one_dir(start_row, start_col, dir_r, dir_c, grid):
            count += 1
    return count

def read_file(file_nm):
    '''
    Returns a two-dimensional array of the seating layout
    of the plane, read from a file.
    '''
    file = open(file_nm, 'r')
    plane_grid = []

    for line in file:
        row = []
        line = line.strip('\n')
        for elem in line:
            row.append(elem)
        plane_grid.append(row)

    file.close()

    return plane_grid

def model_seating(plane_grid):
    '''
    Model the seating arrangement, based on the number of 
    occupies seats adjacent to a seat. 

    Rules:
        If a seat is empty (L) and there are no occupied adjacent to it,
        the seat becomes occupied.
        If a seat is occupied (#) and there are 5 or more seats adjacent
        to it, the seat becomes empty.
        Else, seat's state does not change.

    The modeling stops when there are no more changes to the seating.
    '''
    changes = True
    num_rows = len(plane_grid)
    num_cols = len(plane_grid[0])

    while changes:
        flips = []

        for r in range(num_rows):
            for c in range(num_cols):
                num_occupied = count_occupied_eight_dirs(r, c, plane_grid)
                if plane_grid[r][c] == '#' and num_occupied >= 5:
                    flips.append((r, c, 'L'))
                elif plane_grid[r][c] == 'L' and num_occupied == 0:
                    flips.append((r, c, '#'))
        
        for r, c, val in flips:
            plane_grid[r][c] = val

        changes = len(flips) > 0

def count_occupied_seats(plane_grid):
    '''
    Returns number of occupied seats
    '''
    total = 0
    for r in range(len(plane_grid)):
        for c in range(len(plane_grid[0])):
            if plane_grid[r][c] == '#':
                total += 1
    return total

def solve(file_nm):
    plane_grid = read_file(file_nm)
    model_seating(plane_grid)
    return count_occupied_seats(plane_grid)

def main():
    assert(solve(FILE_TEST_NM) == 26)
    print(solve(FILE_NM))

main()
