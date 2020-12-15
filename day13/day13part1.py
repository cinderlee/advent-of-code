# file = open('day13testinput.txt')
file = open('day13input.txt')

earliest = None

def min_time_bus(lst, earliest):
    sol_time = None
    sol_bus = None

    for elem in lst:
        if elem == 'x':
            continue
        bus_num = int(elem)
        bus_early_val = 0
        if earliest % bus_num > 0:
            bus_early_val = bus_num * (earliest // bus_num + 1)
        else:
            bus_early_val = earliest // bus_num
        if sol_time is None:
            sol_time = bus_early_val
            sol_bus = bus_num
        else:
            sol_time = min(sol_time, bus_early_val)
            if sol_time == bus_early_val:
                sol_bus = bus_num

    return sol_time, sol_bus

for line in file:
    line = line.strip('\n')
    if earliest is None:
        earliest = int(line)
    else:
        lst = line.split(',')
        sol_time, sol_bus = min_time_bus(lst, earliest)
        print((sol_time - earliest) * sol_bus)

file.close()
