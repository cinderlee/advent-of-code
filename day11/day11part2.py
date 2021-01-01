# FILE_NM = 'day11testinput.txt'
FILE_NM = 'day11input.txt'
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def is_valid(row, col, lst):
    return row >= 0 and row < len(lst) and col >= 0 and col < len(lst[0])

def count_occupied_one_dir(row, col, dir_r, dir_c, grid):
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
    count = 0
    for dir_r, dir_c in DIRECTIONS:
        start_row = row + dir_r
        start_col = col + dir_c
        if count_occupied_one_dir(start_row, start_col, dir_r, dir_c, grid):
            count += 1
    return count

def read_file(file_nm):
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
    total = 0
    for r in range(len(plane_grid)):
        for c in range(len(plane_grid[0])):
            if plane_grid[r][c] == '#':
                total += 1
    return total

def main():
    plane_grid = read_file(FILE_NM)
    model_seating(plane_grid)
    print(count_occupied_seats(plane_grid))

main()
