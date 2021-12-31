# Day 9: Encoding Error

INPUT_FILE_NAME = "./inputs/day09input.txt"
TEST_FILE_NAME = "./inputs/day09testinput.txt"

TEST_PREAMBLE_NUM = 5
PREAMBLE_NUM = 25

def read_file_nums(file_nm):
    '''
    Returns a list of numbers from a file.
    '''
    file = open(file_nm, 'r')
    numbers = []
    for line in file:
        line = line.strip('\n')
        numbers.append(int(line))
    file.close()
    return numbers

def is_valid_num(nums_lst, position, preamble_num):
    '''
    Returns whether a number is valid in a list. A valid number is the sum of any 2 previous
    x numbers, where x represents the length of the preamble
    '''
    curr_num = nums_lst[position]
    seen_nums = set()
    for index in range(position - preamble_num, position):
        if curr_num - nums_lst[index] in seen_nums:
            return True
        seen_nums.add(nums_lst[index])
    return False

def find_invalid_num(nums_lst, preamble_num):
    '''
    A preamble of x numbers are first transmitted. Each number afterwards will
    be the sum of any two of the immediately previous x numbers.

    Parameters:
        nums_lst: A list of numbers
        preamble_num: The length of the preamble, x
    
    Returns the invalid number in the list that does not satisfy the rule.
    '''

    pointer = preamble_num
    while pointer < len(nums_lst):
        if not is_valid_num(nums_lst, pointer, preamble_num):
            return nums_lst[pointer]
        pointer += 1

def find_encryption_weakness(nums_lst, target_num):
    '''
    Finds a contiguous set of numbers that add up to the target number,
    which is the invalid number of the list, and returns the encryption
    weakness. The encryption weakness is defined to be the sum of the
    minimum and maximum of the contiguous range.
    '''
    start = 0
    end = 0 
    total = 0
    while end < len(nums_lst):
        if total == target_num:
            break
        elif total > target_num:
            total -= nums_lst[start]
            start += 1
        else:
            total += nums_lst[end]
            end += 1
    
    # set min and max to first number of range
    minimum = nums_lst[start]
    maximum = nums_lst[start]

    # range is from start position to the number before end position
    for index in range(start + 1, end):
        minimum = min(minimum, nums_lst[index])
        maximum = max(maximum, nums_lst[index])

    return minimum + maximum

def solve_part_one(numbers_lst, preamble_num):
    return find_invalid_num(numbers_lst, preamble_num)

def solve_part_two(numbers_lst, preamble_num):
    invalid_num = find_invalid_num(numbers_lst, preamble_num)
    return find_encryption_weakness(numbers_lst, invalid_num)

def main():
    test_numbers_lst = read_file_nums(TEST_FILE_NAME)
    assert(solve_part_one(test_numbers_lst, TEST_PREAMBLE_NUM) == 127)
    assert(solve_part_two(test_numbers_lst, TEST_PREAMBLE_NUM) == 62)

    numbers_lst = read_file_nums(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(numbers_lst, PREAMBLE_NUM))
    print('Part Two:', solve_part_two(numbers_lst, PREAMBLE_NUM))

main()