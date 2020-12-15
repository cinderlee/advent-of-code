# file = open('day13testinput.txt')
file = open('day13input.txt')

line_count = 0
bus_lst = []
for line in file:
    line = line.strip('\n')
    if line_count == 0:
        line_count += 1
        continue
    else:
        lst = line.split(',')
        elem_count = 0
        for elem in lst:
            if elem == 'x':
                elem_count += 1
                continue
            bus_lst.append((int(elem), elem_count))
            elem_count += 1
        print(elem_count)

file.close()
print(bus_lst)
curr_time = 0
acc = 1
for bus_num, disp in bus_lst:
    while (curr_time + disp) % bus_num != 0:
        curr_time += acc
    
    acc *= bus_num

print(curr_time)