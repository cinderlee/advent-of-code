# Day 13: Shuttle Search

INPUT_FILE_NAME = "./inputs/day13input.txt"
TEST_FILE_NAME = "./inputs/day13testinput.txt"

FILE_TEST_NM = 'day13testinput.txt'
FILE_NM = 'day13input.txt'
TEST_BUS_INPUT = '17,x,13,19'
TEST_BUS_INPUT_2 = '67,7,59,61'
TEST_BUS_INPUT_3 = '67,x,7,59,61'
TEST_BUS_INPUT_4 = '67,7,x,59,61'
TEST_BUS_INPUT_5 = '1789,37,47,1889'

def read_file(file_nm):
    '''
    Returns the earliest timestamp you could depart and
    list of bus ids read from a file.
    '''
    file = open(file_nm, 'r')
    earliest_depart_time = int(file.readline())
    bus_ids = file.readline().strip('\n').split(',')
    file.close()
    return earliest_depart_time, bus_ids

def filter_bus_ids(bus_input_lst):
    '''
    Returns list of filtered bus ids where x is excluded.
    '''
    bus_ids_lst = []
    elem_count = 0
    for bus_id in bus_input_lst:
        if bus_id != 'x':
            bus_ids_lst.append((int(bus_id), elem_count))
        elem_count += 1
    return bus_ids_lst

def find_earliest_bus(depart_time, bus_ids):
    '''
    Returns the earliest time and bus id of the earliest bus that 
    can be taken given departure time.
    '''
    earliest_bus_time = None
    earliest_bus_id = None

    for bus_id in bus_ids:
        if bus_id == 'x':
            continue
        bus_id = int(bus_id)
        bus_time = depart_time

        # find next bus time
        if depart_time % bus_id > 0:
            bus_time += bus_id - (depart_time % bus_id)
 
        if earliest_bus_time is None:
            earliest_bus_time = bus_time
            earliest_bus_id = bus_id
        else:
            earliest_bus_time = min(earliest_bus_time, bus_time)
            if earliest_bus_time == bus_time:
                earliest_bus_id = bus_id

    return earliest_bus_time, earliest_bus_id

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

def solve_part_one(earliest_depart_time, bus_ids): 
    '''
    Returns product of id of earliest bus and number of minutes
    you need to wait before it departs.
    '''
    bus_time, bus_id = find_earliest_bus(earliest_depart_time, bus_ids)
    return bus_id * (bus_time - earliest_depart_time)

def solve_part_two(bus_ids):
    bus_ids_filtered = filter_bus_ids(bus_ids)
    return find_earliest_timestamp(bus_ids_filtered)

def run_test_input(test_input):
    '''
    Returns timestamp for test input with only bus id information.
    '''
    test_bus_ids_filtered = filter_bus_ids(test_input.split(','))
    return find_earliest_timestamp(test_bus_ids_filtered)

def main():
    test_earliest_depart_time, test_bus_ids = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_earliest_depart_time, test_bus_ids) == 295)
    assert(solve_part_two(test_bus_ids) == 1068781)

    assert(run_test_input(TEST_BUS_INPUT) == 3417)
    assert(run_test_input(TEST_BUS_INPUT_2) == 754018)
    assert(run_test_input(TEST_BUS_INPUT_3) == 779210)
    assert(run_test_input(TEST_BUS_INPUT_4) == 1261476)
    assert(run_test_input(TEST_BUS_INPUT_5) == 1202161486)

    earliest_depart_time, bus_ids = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(earliest_depart_time, bus_ids))
    print('Part Two:', solve_part_two(bus_ids))

main()
