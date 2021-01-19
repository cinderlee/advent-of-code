FILE_TEST_NM = 'day14testinput.txt'
FILE_NM = 'day14input.txt'

def parse_bitmask(line):
    '''
    The bitmask is a string of 36 bits where most significant
    bit is on the left and least significant is on the right. 
    The bitmask is specified as "mask = ...". 

    Returns a list of tuples in the form of (position, mask bit).
    The X's in the bitmask are excluded from the list.
    '''
    bitmask = []
    line = line.replace('mask = ', '')
    for i in range(len(line)):
        if line[i] == 'X':
            continue
        else:
            bitmask.append((i, line[i]))
    return bitmask

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
    Returns a dictionary of memory information read from a file.
    The dictionary keys are memory locations mapped to a tuple
    of the value to be written at that location and the bitmask
    applied.
    '''
    memory = {}
    bitmask = None

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if 'mask' in line:
            bitmask = parse_bitmask(line)
        else:
            mem_loc, mem_val = parse_memory_info(line)
            memory[mem_loc] = (mem_val, bitmask)
    file.close()

    return memory

def apply_bitmask(bitmask, value):
    '''
    Returns new value in decimal form after applying
    bitmask
    '''
    bin_value = bin(value).replace('0b', '')

    # binary value needs to be padded to be 36 bits
    final_bin_val = ['0' for i in range (36 - len(bin_value))]
    final_bin_val.extend(list(bin_value))
    for index, bit in bitmask:
        final_bin_val[index] = bit
    return int(''.join(final_bin_val), 2)

def get_total_memory_values(memory_dict):
    '''
    Returns the sum of all values in memory after
    applying bitmasks.
    '''
    total = 0
    for mem_loc in memory_dict:
        val, bitmask = memory_dict[mem_loc]
        result_val = apply_bitmask(bitmask, val)
        total += result_val
    return total

def solve(file_nm):
    memory_data = read_file(file_nm)
    return get_total_memory_values(memory_data)

def main():
    assert(solve(FILE_TEST_NM) == 165)
    print(solve(FILE_NM))

main()