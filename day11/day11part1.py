FILE_TEST_NM = 'day11testinput.txt'
FILE_NM = 'day11input.txt'

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
    assert(solve(FILE_TEST_NM) == 37)
    print(solve(FILE_NM))

main()