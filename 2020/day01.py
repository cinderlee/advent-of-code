# Day 1: Expense Report

INPUT_FILE_NAME = "./inputs/day01input.txt"
TEST_FILE_NAME = "./inputs/day01testinput.txt"

def read_expenses_file(file_nm):
    '''
    Returns a list of expenses, read in from a file.
    '''
    file = open(file_nm, 'r')
    expenses = [int(expense) for expense in file.read().split('\n')]
    file.close()
    return expenses

def get_three_addends(expenses, goal):
    '''
    Returns three addends whose sum is the goal
    '''

    for index in range(len(expenses)):
        first_num = expenses[index]
        sub_sum = goal - first_num

        for index2 in range(index + 1, len(expenses)):
            if sub_sum - expenses[index2] in expenses:
                return first_num, expenses[index2], sub_sum - expenses[index2]

def solve_part_one(expenses):
    '''
    Returns product of two numbers in the file that add up to 2020
    '''
    for number in expenses:
        if 2020 - number in expenses:
            return(number * (2020 - number))

def solve_part_two(expenses):
    '''
    Returns product of the three numbers that add up to 2020
    '''
    num_one, num_two, num_three = get_three_addends(expenses, 2020)
    return num_one * num_two * num_three

def main():
    test_expenses = read_expenses_file(TEST_FILE_NAME)
    assert(solve_part_one(test_expenses) == 514579)
    assert(solve_part_two(test_expenses) == 241861950)

    expenses = read_expenses_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(expenses))
    print('Part Two:', solve_part_two(expenses))

main()