# FILE_NM = 'day10testinput.txt'
FILE_NM = 'day10input.txt'

def read_file(file_nm):
    adapter_jolts = [0]
    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        adapter_jolts.append(int(line))
    file.close()

    adapter_jolts.sort()

    return adapter_jolts

def count_jolt_differences(adapter_jolts_lst):
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

def main():
    adapter_jolts = read_file(FILE_NM)
    one_jolt_diff, three_jolt_diff = count_jolt_differences(adapter_jolts)
    print(one_jolt_diff * three_jolt_diff)

main()
