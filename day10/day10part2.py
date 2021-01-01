# FILE_NM = 'day10testinput.txt'
FILE_NM = 'day10input.txt'

def read_file(file_nm):
    adapter_jolts = []
    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        adapter_jolts.append(int(line))
    file.close()

    adapter_jolts.sort()

    return adapter_jolts

def count_distinct_paths(adapter_jolts_lst):
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

def main():
    adapter_jolts = read_file(FILE_NM)
    print(count_distinct_paths(adapter_jolts))

main()



