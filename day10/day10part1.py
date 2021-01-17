FILE_TEST_NM = 'day10testinput.txt'
FILE_TEST_NM_2 = 'day10testinput2.txt'
FILE_NM = 'day10input.txt'

def read_file(file_nm):
    '''
    Returns a sorted list of joltage numbers read from a file.
    Note: Charging outlet near seat has joltage rating of 0.
    '''
    adapter_jolts = [0]
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

def solve(file_nm):
    '''
    You have a list of joltage adapters, and any adapter can take
    an input of 1-3 jolts lower than its rating. Your device has a 
    built-in joltage adapter that is 3 jolts higher than the 
    highest-rated adapter. All adapters are used to charge device.

    Returns the product of number of 1-jolt differences and 
    number of 3-jolt differences. 
    '''
    adapter_jolts = read_file(file_nm)
    one_jolt_diff, three_jolt_diff = count_jolt_differences(adapter_jolts)
    return one_jolt_diff * three_jolt_diff

def main():
    assert(solve(FILE_TEST_NM) == 35)
    assert(solve(FILE_TEST_NM_2) == 220)
    print(solve(FILE_NM))


main()
