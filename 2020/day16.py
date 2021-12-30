# Day 16: Ticket Translation

INPUT_FILE_NAME = "./inputs/day16input.txt"
TEST_FILE_NAME = "./inputs/day16testinput.txt"
TEST_FILE_NAME_2 = "./inputs/day16testinput2.txt"

def get_valid_numbers(interval_string):
    '''
    Returns a list of valid numbers given an interval in string
    notations.
    '''
    start, end = tuple(int(num) for num in interval_string.split('-'))
    return [val for val in range(start, end + 1)]

def parse_rule(line):
    '''
    Returns a dictionary of the field mapped to its valid values.
    '''
    field, intervals = line.split(': ')
    interval_one, interval_two = intervals.split(' or ')

    valid_numbers = get_valid_numbers(interval_one)
    valid_numbers.extend(get_valid_numbers(interval_two))
    return {field: valid_numbers}, set(valid_numbers)

def read_file(file_nm):
    '''
    Returns dictionary of rules where the field is mapped to its 
    valid values, list of all valid vlaues, your ticket information,
    and nearby tickets information.
    '''
    rules_section = True
    your_ticket_section = False
    nearby_tickets_section = False
    rules = {}
    valid_numbers = set()
    your_ticket = []
    nearby_tickets = []

    file = open(file_nm, 'r')
    for line in file:
        line = line.strip('\n')
        if not line:
            continue
        elif 'your ticket' in line:
            your_ticket_section = True
            rules_section = False
        elif 'nearby tickets' in line:
            nearby_tickets_section = True
            your_ticket_section = False
        elif rules_section:
            rule, valid_numbers_subset = parse_rule(line)
            rules.update(rule)
            valid_numbers.update(valid_numbers_subset)
        else:
            # turn line into tuple of numbers
            ticket = tuple(int(num) for num in line.split(','))
            if your_ticket_section:
                your_ticket = ticket
            else:
                nearby_tickets.append(ticket)
    file.close()

    return rules, valid_numbers, your_ticket, nearby_tickets

def is_valid_ticket(nearby_ticket, valid_set):
    '''
    Checks if nearby ticket is a valid ticket
    '''
    for value in nearby_ticket:
        if value not in valid_set:
            return False
    return True

def get_invalid_nums(nearby_tickets, valid_set):
    '''
    Returns list of invalid numbers of all the nearby tickets.
    '''
    invalid_numbers = []
    for ticket in nearby_tickets:
        for value in ticket:
            if value not in valid_set:
                invalid_numbers.append(value)
    return invalid_numbers

def filter_nearby_tickets(nearby_tickets, valid_set):
    '''
    Filters and returns an updated list of nearby tickets.
    '''
    updated_nearby_tickets = []
    for ticket in nearby_tickets:
        if is_valid_ticket(ticket, valid_set):
            updated_nearby_tickets.append(ticket)
    return updated_nearby_tickets

def get_valid_values_per_field(nearby_tickets):
    '''
    Given a list of valid nearby tickets, returns a list of lists 
    where each list contains all valid values for one field collectively. Fields
    are in the same order for all tickets.
    '''
    valid_fields_values = [[] for field in range(len(nearby_tickets[0]))]
    for ticket in nearby_tickets:
        for i in range(len(ticket)):
            valid_fields_values[i].append(ticket[i])

    return valid_fields_values

def match_fields(rules, valid_fields_values):
    '''
    Returns a dictionary of fields mapped to their positions (index) on a ticket.
    '''
    fields_key = {}
    for field in rules:
        fields_key[field] = []

    for index in range(len(valid_fields_values)):
        valid_sub_lst = valid_fields_values[index]
        for field in rules:
            could_be_field = True
            for number in valid_sub_lst:
                if number not in rules[field]:
                    could_be_field = False
                    break
            if could_be_field:
                fields_key[field].append(index)

    index_confirmed = set()
    while len(index_confirmed) != len(fields_key):
        index = None
        for field in fields_key:
            if len(fields_key[field]) == 1 and fields_key[field][0] not in index_confirmed:
                index = fields_key[field][0]
                break
        
        for field in fields_key:
            if len(fields_key[field]) == 1:
                continue
            if index in fields_key[field]:
                fields_key[field].remove(index)

        index_confirmed.add(index)

    return fields_key

def retrieve_index_list(fields_dict, sub_key_phrase):
    '''
    Returns list of positions of fields containing a subphrase.
    '''
    index_lst = []
    for field in fields_dict:
        if sub_key_phrase in field:
            index_lst.extend(fields_dict[field])
    return index_lst

def solve_part_one(nearby_tickets, valid_numbers):
    '''
    Returns sum of all invalid values, excluding your ticket.
    '''
    return sum(get_invalid_nums(nearby_tickets, valid_numbers))

def solve_part_two(rules, valid_numbers, your_ticket, nearby_tickets):
    '''
    Returns sum of all invalid values, excluding your ticket.
    '''
    nearby_tickets = filter_nearby_tickets(nearby_tickets, valid_numbers)
    valid_fields_values = get_valid_values_per_field(nearby_tickets)
    fields_info = match_fields(rules, valid_fields_values)
    departure_list = retrieve_index_list(fields_info, 'departure')

    acc = 1
    for elem in departure_list:
        acc *= your_ticket[elem]
    return acc

def run_test_file(file_nm):
    '''
    Returns field positions given a test file
    '''
    rules, valid_numbers, your_ticket, nearby_tickets = read_file(file_nm)
    nearby_tickets = filter_nearby_tickets(nearby_tickets, valid_numbers)
    valid_fields_values = get_valid_values_per_field(nearby_tickets)
    fields_info = match_fields(rules, valid_fields_values)
    return fields_info

def main():
    test_rules, test_valid_numbers, test_your_ticket, test_nearby_tickets = read_file(TEST_FILE_NAME)
    assert(solve_part_one(test_nearby_tickets, test_valid_numbers) == 71)
    assert(run_test_file(TEST_FILE_NAME_2) == {'row': [0], 'class': [1], 'seat': [2]})

    rules, valid_numbers, your_ticket, nearby_tickets = read_file(INPUT_FILE_NAME)
    print('Part One:', solve_part_one(nearby_tickets, valid_numbers))
    print('Part Two:', solve_part_two(rules, valid_numbers, your_ticket, nearby_tickets))

main()
