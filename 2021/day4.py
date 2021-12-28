# Day 4: Giant Squid

INPUT_FILE_NAME = "./inputs/day4input.txt"
TEST_FILE_NAME = "./inputs/day4testinput.txt"

class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.elements = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.elements[(i, j)] = board[i][j]

    def mark_number(self, number):
        '''
        If a number exists on a board, number is marked with an X
        '''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == number:
                    self.board[i][j] = "X"
                    return self.determine_win(i, j)
        return False

    def determine_win(self, i, j):
        '''
        Checks if there is a Bingo win after marking a number at 
        row i and column j. Diagonal wins do not count.
        '''
        col_win = True
        row_win = True

        for row in range(len(self.board)):
            if self.board[row][j] != 'X':
                col_win = False
                break
        
        for col in range(len(self.board[0])):
            if self.board[i][col] != 'X':
                row_win = False
                break
        
        return col_win or row_win

    def calculate_sum_unmarked_numbers(self):
        '''
        Returns sum of numbers that are unmarked.
        '''
        total = 0
        for row in self.board:
            for elem in row:
                if elem != 'X':
                    total += int(elem)

        return total

    def reset(self):
        '''
        Resets board
        '''
        for position, val in self.elements.items():
            row, col = position
            self.board[row][col] = val
        

def parse_file(file_nm):
    '''
    Returns a list of drawn numbers and a list of bingo boards that are read from a file.
    '''
    file = open(file_nm, 'r')

    drawn_numbers = file.readline().strip('\n').split(',')
    file.readline()

    boards = []
    board = []
    for line in file:
        line = line.strip('\n')

        if line == '':
            boards.append(BingoBoard(board))
            board = []
            continue
            
        board_row = []
        row = line.strip('\n').split(' ')
        for elem in row:
            if elem != '':
                board_row.append(elem)

        board.append(board_row)

    # add the last board
    boards.append(BingoBoard(board))

    file.close()
    return drawn_numbers, boards

def solve_part_one(drawn_numbers, boards):
    '''
    Returns the score of the first winning board from calling a set of drawn
    numbers. The score is the product of the number that was drawn and 
    the sum of unmarked numbers on the winning board.
    '''
    for number in drawn_numbers:
        for board in boards:
            is_winner = board.mark_number(number)
            if is_winner:
                return board.calculate_sum_unmarked_numbers() * int(number)

def solve_part_two(drawn_numbers, boards):
    '''
    Returns the score of the last winning board from calling a set of drawn
    numbers. The score is the product of the number that was drawn and 
    the sum of unmarked numbers on the winning board.
    '''
    last_index = len(boards) - 1
    for number in drawn_numbers:
        curr_index = 0
        
        while curr_index <= last_index:
            is_winner = boards[curr_index].mark_number(number)
            if is_winner:
                # move winning board to the end
                boards[curr_index], boards[last_index] = boards[last_index], boards[curr_index]
                last_index -= 1
            else:
                curr_index += 1

            if last_index == -1:
                return boards[0].calculate_sum_unmarked_numbers() * int(number)

def main():
    test_drawn_numbers, test_boards = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_drawn_numbers, test_boards) == 4512)

    drawn_numbers, boards = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(drawn_numbers, boards))
    for board in boards:
        board.reset()
    print('Part Two:', solve_part_two(drawn_numbers, boards))

main()
