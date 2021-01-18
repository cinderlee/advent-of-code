FILE_TEST_NM = 'day13testinput.txt'
FILE_NM = 'day13input.txt'

def read_file(file_nm):
    '''
    Returns the earliest timestamp you could depart and
    list of bus ids read from a file.
    '''
    earliest_depart_time = None
    bus_ids = None
    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if earliest_depart_time is None:
            earliest_depart_time = int(line)
        else:
            bus_ids = line.split(',')
    file.close()
    return earliest_depart_time, bus_ids

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

def solve(file_nm):
    '''
    Returns product of id of earliest bus and number of minutes
    you need to wait before it departs.
    '''
    earliest_depart_time, bus_ids = read_file(file_nm)
    bus_time, bus_id = find_earliest_bus(earliest_depart_time, bus_ids)
    return bus_id * (bus_time - earliest_depart_time)

def main():
    assert(solve(FILE_TEST_NM) == 295)
    print(solve(FILE_NM))

main()