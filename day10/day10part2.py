FILE_TEST_NM = 'day10testinput.txt'
FILE_TEST_NM_2 = 'day10testinput2.txt'
FILE_NM = 'day10input.txt'

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

def solve(file_nm):
    '''
    You have a list of joltage adapters, and any adapter can take
    an input of 1-3 jolts lower than its rating. Your device has a 
    built-in joltage adapter that is 3 jolts higher than the 
    highest-rated adapter. 
    '''
    adapter_jolts = read_file(file_nm)
    return count_distinct_paths(adapter_jolts)

def main():
    assert(solve(FILE_TEST_NM) == 8)
    assert(solve(FILE_TEST_NM_2) == 19208)
    print(solve(FILE_NM))

main()



