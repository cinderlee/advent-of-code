# Day 11: Seating System

import copy

INPUT_FILE_NAME = "./inputs/day11input.txt"
TEST_FILE_NAME = "./inputs/day11testinput.txt"

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def read_file(file_nm):
    '''
    Returns a two-dimensional array of the seating layout
    of the plane, read from a file.
    '''
    file = open(file_nm, 'r')
    plane_grid = []

    for line in file:
        row = [seat for seat in line.strip('\n')]
        plane_grid.append(row)

    file.close()

    return plane_grid

def is_valid(row, col, lst):
    '''
    Returns whether row and col are valid indices.
    '''
    return row >= 0 and row < len(lst) and col >= 0 and col < len(lst[0])

def count_occupied_adjacent_seats(row, col, grid):
    '''
    Returns number of occupied adjacent seats given a
    seat location
    '''
    count = 0
    for r in range(row - 1, row + 2):
        for c in range (col - 1, col + 2):
            if r == row and c == col:
                continue
            if not is_valid(r, c, grid):
                continue
            if grid[r][c] == '#':
                count += 1
    return count

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

def model_seating_part_one(plane_grid):
    '''
    Model the seating arrangement, based on the number of 
    occupies seats adjacent to a seat. 

    Rules:
        If a seat is empty (L) and there are no occupied adjacent to it,
        the seat becomes occupied.
        If a seat is occupied (#) and there are 4 or more seats adjacent
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
                num_occupied = count_occupied_adjacent_seats(r, c, plane_grid)
                if plane_grid[r][c] == '#' and num_occupied >= 4:
                    flips.append((r, c, 'L'))
                elif plane_grid[r][c] == 'L' and num_occupied == 0:
                    flips.append((r, c, '#'))
        
        for r, c, val in flips:
            plane_grid[r][c] = val

        changes = len(flips) > 0

def model_seating_part_two(plane_grid):
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

def solve_part_one(plane_grid):
    model_seating_part_one(plane_grid)
    return count_occupied_seats(plane_grid)

def solve_part_two(plane_grid):
    model_seating_part_two(plane_grid)
    return count_occupied_seats(plane_grid)

def main():
    test_plane_grid = read_file(TEST_FILE_NAME)
    test_plane_grid_copy = copy.deepcopy(test_plane_grid)
    assert(solve_part_one(test_plane_grid) == 37)
    assert(solve_part_two(test_plane_grid_copy) == 26)
    
    plane_grid = read_file(INPUT_FILE_NAME)
    plane_grid_copy = copy.deepcopy(plane_grid)
    print('Part One:', solve_part_one(plane_grid))
    print('Part Two:', solve_part_two(plane_grid_copy))

main()
