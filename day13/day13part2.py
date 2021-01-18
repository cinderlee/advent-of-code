FILE_TEST_NM = 'day13testinput.txt'
FILE_NM = 'day13input.txt'
TEST_BUS_INPUT = '17,x,13,19'
TEST_BUS_INPUT_2 = '67,7,59,61'
TEST_BUS_INPUT_3 = '67,x,7,59,61'
TEST_BUS_INPUT_4 = '67,7,x,59,61'
TEST_BUS_INPUT_5 = '1789,37,47,1889'

def parse_bus_ids(bus_input):
    '''
    Returns list of bus ids from given input.
    '''
    bus_ids_lst = []
    lst = bus_input.strip('\n').split(',')
    elem_count = 0
    for bus_id in lst:
        if bus_id != 'x':
            bus_ids_lst.append((int(bus_id), elem_count))
        elem_count += 1
    return bus_ids_lst

def read_file(file_nm):
    '''
    Returns list of bus ids read from a file.
    '''
    file = open(file_nm, 'r')
    file.readline()     # skip first line
    bus_ids_line = file.readline()
    bus_ids = parse_bus_ids(bus_ids_line)
    file.close()

    return bus_ids

def find_earliest_timestamp(bus_ids):
    '''
    Returns earliest timestamp where the first bus id departs 
    at that time and each subsequent bus id departs at that minute.
    '''
    curr_time = 0
    lowest_common_multiple = 1
    for bus_id, disp in bus_ids:
        while (curr_time + disp) % bus_id != 0:
            curr_time += lowest_common_multiple
        lowest_common_multiple *= bus_id
    return curr_time

def solve(file_nm):
    bus_ids = read_file(file_nm)
    return find_earliest_timestamp(bus_ids)

def run_test_input(test_input):
    '''
    Returns timestamp for test input with only bus id information.
    '''
    bus_ids = parse_bus_ids(test_input)
    return find_earliest_timestamp(bus_ids)

def main():
    assert(solve(FILE_TEST_NM) == 1068781)
    assert(run_test_input(TEST_BUS_INPUT) == 3417)
    assert(run_test_input(TEST_BUS_INPUT_2) == 754018)
    assert(run_test_input(TEST_BUS_INPUT_3) == 779210)
    assert(run_test_input(TEST_BUS_INPUT_4) == 1261476)
    assert(run_test_input(TEST_BUS_INPUT_5) == 1202161486)
    print(solve(FILE_NM))

main()
