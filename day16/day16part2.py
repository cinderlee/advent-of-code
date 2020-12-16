# file = open('day16testinput.txt')
file = open('day16input.txt')

rules = {}
valid_nums = set()
lst = []

your_ticket = False
ticket = None

nearby_tickets = False
valid_nearby_parts = []

def add_valid_vals(interval_one, interval_two, vals_set, rule_dict, key):
    lst = interval_one.split('-')
    start = int(lst[0])
    end = int(lst[1])
    valid_num_lst = []

    for i in range(start, end + 1):
        vals_set.add(i)
        valid_num_lst.append(i)

    lst = interval_two.split('-')
    start = int(lst[0])
    end = int(lst[1])

    for i in range(start, end + 1):
        vals_set.add(i)
        valid_num_lst.append(i)
    
    rule_dict[key] = valid_num_lst

def parse_rule_line(string, valid_nums_set, rule_dict):
    string = string.split(': ')
    key = string[0]
    val_string = string[1].split(' or ')
    add_valid_vals(val_string[0], val_string[1], valid_nums_set, rule_dict, key)

def check_ticket(string, valid_nums_set):
    lst_nums = string.split(',')
    for elem in lst_nums:
        if int(elem) not in valid_nums_set:
            return False, lst_nums
    return True, lst_nums

def retrieve_index_set(valid_dict, sub_key_phrase):
    index_set = set()
    for ticket_key in valid_dict:
        if sub_key_phrase in ticket_key:
            for elem in valid_dict[ticket_key]:
                index_set.add(elem)
    return index_set

def count_keys_match_subphrase(valid_dict, sub_key_phrase):
    key_count = 0
    for key in valid_dict:
        if sub_key_phrase in key:
            key_count += 1
    return key_count

def check_done(valid_dict):
    sub_key_phrase = 'departure'
    sub_set = retrieve_index_set(valid_dict, sub_key_phrase)
    sub_key_count = count_keys_match_subphrase(valid_dict, sub_key_phrase)
    return len(sub_set) == sub_key_count


for line in file:
    line = line.strip('\n')
    if not line:
        continue
    if 'or' in line:
        parse_rule_line(line, valid_nums, rules)
    elif 'your ticket' in line:
        your_ticket = True
    elif 'nearby tickets' in line:
        nearby_tickets = True
        your_ticket = False
        for i in range(len(rules)):
            valid_nearby_parts.append([])
    elif your_ticket:
        ticket = line.split(',')
        for index in range(len(ticket)):
            ticket[index] = int(ticket[index])
    elif nearby_tickets:
        is_valid, lst = check_ticket(line, valid_nums)
        if is_valid:
            for i in range(len(lst)):
                valid_nearby_parts[i].append(int(lst[i]))

file.close()

keys_index = {}
for key in rules:
    keys_index[key] = []

counter = 0 
while counter < len(valid_nearby_parts):
    valid_lst = []
    elem = valid_nearby_parts[counter]
    for key in rules:
        valid_key = True
        for e in elem:
            if e in rules[key]:
                continue
            valid_key = False
            break
        if valid_key:
            keys_index[key].append(counter)
    counter += 1

index_confirmed = set()
while True:
    if len(index_confirmed) == len(rules) - count_keys_match_subphrase(keys_index, 'departure'):
        break

    for key in keys_index:
        if len(keys_index[key]) == 1:
            index_confirmed.add(keys_index[key][0])

    for elem in index_confirmed:
        for key in keys_index:
            if len(keys_index[key]) == 1:
                continue
            if elem in keys_index[key]:
                keys_index[key].remove(elem)


index_depart_set = retrieve_index_set(keys_index, 'departure')

total = 1
for elem in index_depart_set:
    total *= ticket[elem]
print(total)
