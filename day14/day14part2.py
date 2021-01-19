FILE_TEST_NM = 'day14testinput2.txt'
FILE_NM = 'day14input.txt'

def parse_bitmask(line):
    '''
    The bitmask is a string of 36 bits where most significant
    bit is on the left and least significant is on the right. 
    The bitmask is specified as "mask = ...". 

    Returns the bitmask stripped of 0's on the left side.
    '''
    line = line.replace('mask = ', '')
    # 0's in the bitmask do not make changes
    return line.lstrip('0')

def parse_memory_info(line):
    '''
    The program attempts to store a value at a memory address. The
    line will be written as "mem[location] = value".

    Returns the location and value as a list.
    '''
    line = line.replace('mem[', '').replace(']', '')
    mem_data = line.split(' = ')
    return int(mem_data[0]), int(mem_data[1])

def read_file(file_nm):
    '''
    Returns a list of tuples of memory information containing
    (memory location, bitmask, value).
    '''
    memory_info = []
    bitmask = None

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if 'mask' in line:
            bitmask = parse_bitmask(line)
        else:
            mem_loc, mem_val = parse_memory_info(line)
            memory_info.append((mem_loc, bitmask, mem_val))
    file.close()

    return memory_info

def pad_bin_num(bin_num, bit_length):
    '''
    Pads a binary string with 0's in front to match 
    a specified string length
    '''
    padded_zeroes = '0' * (bit_length - len(bin_num))
    return padded_zeroes + bin_num

def get_x_combos(num_x):
    '''
    X is a floating bit, which takes on all values. 
    Given the number of X's in the bitmask, returns the
    different combinations the X's can be. 

    Example:
    If there are 3 X's, then the binary values of 0-7 
    are valid cominations.
    '''
    x_combinations = []
    for num in range(0, 2 ** num_x):
        combo = bin(num).replace('0b', '')
        # need to pad them to number of x's in bitmask
        combo = pad_bin_num(combo, num_x)
        x_combinations.append(combo)
    return x_combinations

def get_final_binary_form(mem_loc_bin, bitmask):
    '''
    Returns the final binary form of memory location and the locations
    of the floating bits (X).

    Rules:
        If bitmask bit is 0, memory address bit is unchanged.
        If bitmask bit is 1, memory address bit is overwritten with 1.
        If bitmask bit is X, memory address bit is floating.
    '''
    final_binary = []
    x_locs = []
    for i in range(len(bitmask)):
        if bitmask[i] == 'X' or bitmask[i] == '1':
            if bitmask[i] == 'X':
                x_locs.append(i)
            final_binary.append(bitmask[i])
        else:
            final_binary.append(mem_loc_bin[i])

    return final_binary, x_locs

def find_all_locs(mem_loc, bitmask):
    '''
    Applies bitmask to given memory location and returns all 
    decoded memory locations. 
    '''
    mem_loc_bin = bin(mem_loc).replace('0b', '')

    # pad the strings to be of same length
    length = max(len(bitmask), len(mem_loc_bin))
    mem_loc_bin = pad_bin_num(mem_loc_bin, length)
    bitmask = pad_bin_num(bitmask, length)

    final_binary, x_locs = get_final_binary_form(mem_loc_bin, bitmask)
    x_combos = get_x_combos(len(x_locs))
    
    locs = []
    for x_combo in x_combos:
        for i in range(len(x_locs)):
            # sub in the combo numbers for the x's
            final_binary[x_locs[i]] = x_combo[i]
        locs.append(int(''.join(final_binary), 2))

    return locs

def set_memory(memory_info):
    '''
    Returns dictionary of memory locations mapped to
    value after applying bitmask to original memory location.
    '''
    memory = {}
    for mem_loc, bitmask, mem_val in memory_info:
        all_mem_locs = find_all_locs(mem_loc, bitmask)
        for loc in all_mem_locs:
            memory[loc] = mem_val
    return memory

def get_total_memory_values(memory_dict):
    '''
    Returns the sum of all values in memory after
    applying bitmasks.
    '''
    return sum(memory_dict.values())

def solve(file_nm):
    memory_data = read_file(file_nm)
    memory_dict = set_memory(memory_data)
    return get_total_memory_values(memory_dict)

def main():
    assert(solve(FILE_TEST_NM) == 208)
    print(solve(FILE_NM))

main()