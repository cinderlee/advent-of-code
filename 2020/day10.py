# Day 10: Adapter Array

INPUT_FILE_NAME = "./inputs/day10input.txt"
TEST_FILE_NAME = "./inputs/day10testinput.txt"
TEST_FILE_NAME_2 = "./inputs/day10testinput2.txt"

def read_file(file_nm):
    '''
    Returns a sorted list of joltage numbers read from a file.
    Note: Charging outlet near seat has joltage rating of 0.
    '''
    adapter_jolts = []
    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        adapter_jolts.append(int(line))
    file.close()

    adapter_jolts.sort()

    return adapter_jolts

def count_jolt_differences(adapter_jolts_lst):
    '''
    Returns a tuple representing number of joltage differences of 1
    and joltage differences of 3 between charging outlet, adapters,
    and device.
    '''
    one_jolt_diff = 0
    three_jolt_diff = 0
    for i in range(1, len(adapter_jolts_lst)):
        diff = adapter_jolts_lst[i] - adapter_jolts_lst[i - 1]
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1

    # add one more for the diff between the last number and the device adaptor
    three_jolt_diff += 1

    return one_jolt_diff, three_jolt_diff

def count_distinct_paths(adapter_jolts_lst):
    '''
    Returns the number of different ways adapters can be arranged
    that will connect charging outlet to device.
    '''
    # Only store the number of paths for the adapters
    # within range of 3 jolts of current adapter
    num_path_one = 0 
    num_path_two = 0 
    num_path_three = 1
    for num in range(1, max(adapter_jolts_lst) + 1):
        num_paths_curr = 0
        if num in adapter_jolts_lst:
            num_paths_curr = num_path_one + num_path_two + num_path_three
        
        num_path_one = num_path_two
        num_path_two = num_path_three
        num_path_three = num_paths_curr

    return num_path_three

def solve_part_one(adapter_jolts):
    '''
    You have a list of joltage adapters, and any adapter can take
    an input of 1-3 jolts lower than its rating. Your device has a 
    built-in joltage adapter that is 3 jolts higher than the 
    highest-rated adapter. All adapters are used to charge device.

    Returns the product of number of 1-jolt differences and 
    number of 3-jolt differences. 
    '''
    # List passed to count_jolt_differences include 0 for charging outlet
    one_jolt_diff, three_jolt_diff = count_jolt_differences([0] + adapter_jolts)
    return one_jolt_diff * three_jolt_diff

def solve_part_two(adapter_jolts):
    '''
    You have a list of joltage adapters, and any adapter can take
    an input of 1-3 jolts lower than its rating. Your device has a 
    built-in joltage adapter that is 3 jolts higher than the 
    highest-rated adapter. 
    '''
    return count_distinct_paths(adapter_jolts)

def main():
    test_adapter_jolts = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_adapter_jolts) == 35)
    assert(solve_part_two(test_adapter_jolts) == 8)

    test_adapter_jolts_2 = read_file(TEST_FILE_NAME_2)  
    assert(solve_part_one(test_adapter_jolts_2) == 220)  
    assert(solve_part_two(test_adapter_jolts_2) == 19208)

    adapter_jolts = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(adapter_jolts))
    print('Part Two:', solve_part_two(adapter_jolts))

main()



