# file = open('day16testinput.txt')
file = open('day16input.txt')

def read_file(file_nm):
    rules_section = True
    your_ticket_section = False
    nearby_tickets_section = False

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if not line:
            continue
        if rules_section:
            line = line.split(': ')
            val_string = line[1].split(' or ')

            part1 = val_string[0]
            add_valid_vals(part1, valid_nums)

            part2 = val_string[1]
            add_valid_vals(part2, valid_nums)
        elif 'your ticket' in line:
            your_ticket = True
        elif 'nearby tickets' in line:
            nearby_tickets = True
            your_ticket = False
        elif your_ticket:
            continue
        elif nearby_tickets:
            add_invalid_nums(line, valid_nums, invalid_nums)
    file.close()

valid_nums = set()
invalid_nums = []

def add_valid_vals(string, vals_set):
    lst = string.split('-')
    start = int(lst[0])
    end = int(lst[1])
    for i in range(start, end + 1):
        vals_set.add(i)

def add_invalid_nums(string, valid_set, invalid_lst):
    lst_nums = string.split(',')
    for elem in lst_nums:
        if int(elem) not in valid_set:
            invalid_lst.append(int(elem))


for line in file:
    line = line.strip('\n')
    if not line:
        continue
    if 'or' in line:
        line = line.split(': ')
        val_string = line[1].split(' or ')

        part1 = val_string[0]
        add_valid_vals(part1, valid_nums)

        part2 = val_string[1]
        add_valid_vals(part2, valid_nums)
    elif 'your ticket' in line:
        your_ticket = True
    elif 'nearby tickets' in line:
        nearby_tickets = True
        your_ticket = False
    elif your_ticket:
        continue
    elif nearby_tickets:
        add_invalid_nums(line, valid_nums, invalid_nums)

file.close()

print(sum(invalid_nums))
