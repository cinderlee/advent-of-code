# Day 1: Sonar Sweep

INPUT_FILE_NAME = "./inputs/day01input.txt"
TEST_FILE_NAME = "./inputs/day01testinput.txt"

def parse_file(file_nm):
    '''
    Returns a list of sea depth measurements retrieved from the sonar sweep.
    '''
    numbers_lst = []

    file = open(file_nm)
    for line in file:
        numbers_lst.append(int(line.strip('\n')))
    file.close()

    return numbers_lst

def count_increased_measurements(numbers_lst):
    '''
    Counts the number of times a depth measurement increases from 
    the previous measurement.
    '''
    counter = 0
    curr = numbers_lst[0]

    for i in range(1, len(numbers_lst)):
        if numbers_lst[i] > curr:
            counter += 1
        curr = numbers_lst[i]
    return counter

def count_increased_sums(numbers_lst):
    '''
    Counts the number of times the sum of depth measurements in a 
    three-measurement sliding-window increases from the previous sum.
    '''
    counter = 0
    sliding_window = numbers_lst[:3]
    curr_sum = sum(sliding_window)
    counter = 0

    for i in range(3, len(numbers_lst)):
        sliding_window[0], sliding_window[1] = sliding_window[1], sliding_window[2]
        sliding_window[2] = numbers_lst[i]

        if sum(sliding_window) > curr_sum:
            counter += 1

        curr_sum = sum(sliding_window)
    return counter

def solve_part_one(numbers_lst):
    return count_increased_measurements(numbers_lst)

def solve_part_two(numbers_lst):
    return count_increased_sums(numbers_lst)

def main():
    test_numbers_lst = parse_file(TEST_FILE_NAME)
    assert(solve_part_one(test_numbers_lst) == 7)
    assert(solve_part_two(test_numbers_lst) == 5)

    numbers_lst = parse_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(numbers_lst))
    print('Part Two:', solve_part_two(numbers_lst))

main()
